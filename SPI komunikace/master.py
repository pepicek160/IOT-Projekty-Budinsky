from machine import Pin, SPI
import time

# SPI konfigurace (Master)
spi = SPI(0, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    if not button.value():
        cs.value(0)  
        spi.write(b'1')  
        cs.value(1)
        print("Odesláno: 1")
        time.sleep(0.5)
