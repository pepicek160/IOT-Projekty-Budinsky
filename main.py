from machine import Pin, PWM
import time, urandom

# LED piny
red = Pin(4, Pin.OUT)
yellow = Pin(3, Pin.OUT)
green = Pin(2, Pin.OUT)

# Buzzer pin s PWM
buzzer = PWM(Pin(5))

leds = [red, yellow, green]

def buzz(duration=0.1, freq=4000):
    buzzer.freq(freq)       # frekvence v Hz
    buzzer.duty_u16(32768)  # 50% hlasitost (rozsah 0–65535)
    time.sleep(duration)
    buzzer.duty_u16(0)      # vypnout

while True:
    # Vyber náhodnou LED
    led = leds[urandom.getrandbits(2) % len(leds)]
    
    # Rozsviť ji
    led.value(1)
    buzz(0.05, 2000)  # krátké pípnutí
    time.sleep(urandom.getrandbits(3) / 10)  # 0–0.7 s
    
    # Zhasni ji
    led.value(0)
    time.sleep(urandom.getrandbits(4) / 10)  # 0–1.5 s
