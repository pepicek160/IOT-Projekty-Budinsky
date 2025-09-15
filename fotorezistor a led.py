from machine import Pin, ADC, PWM
import utime

# --- Světelný senzor (LDR) ---
class LightSensor:
    def __init__(self, adc_pin):
        self.adc = ADC(Pin(adc_pin))
        self.min_val = 65535   # pro kalibraci
        self.max_val = 0

    def read_raw(self):
        val = self.adc.read_u16()
        # Uloží min a max pro kalibraci
        if val < self.min_val:
            self.min_val = val
        if val > self.max_val:
            self.max_val = val
        return val

    def read_normalized(self):
        """Vrací hodnotu 0–100 % podle kalibrace"""
        raw = self.read_raw()
        span = max(1, self.max_val - self.min_val)
        return int(((raw - self.min_val) / span) * 100)

# --- LED řízení (PWM) ---
class AutoLightControl:
    def __init__(self, light_sensor, led_pin):
        self.sensor = light_sensor
        self.led = PWM(Pin(led_pin))
        self.led.freq(1000)

    def update(self):
        light_pct = self.sensor.read_normalized()
        brightness = 100 - light_pct  # inverze
        duty = int((brightness / 100) * 65535)
        self.led.duty_u16(duty)
        print(f"Světlo: {light_pct}% → LED jas: {brightness}%")


light = LightSensor(26)      # GP26 = ADC0
led = AutoLightControl(light, 15)  # GP15 = LED PWM

print("Začíná kalibrace... Pohybuj se světlem před senzorem.")
for i in range(50):  # krátká kalibrace
    light.read_raw()
    utime.sleep(0.1)

print("Kalibrace hotova. Spouštím regulaci jasu LED.\n")

while True:
    led.update()
    utime.sleep(0.2)
