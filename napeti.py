from machine import Pin, ADC
import utime

ldr = ADC(Pin(26))

while True:
    raw = ldr.read_u16() 
    voltage = (raw / 65535) * 3.3  # přepočet na napětí
    print(f"ADC: {raw} | Napětí: {voltage:.2f} V")
    utime.sleep(0.2)
