from machine import Pin, SPI
import time

# SPI konfigurace (Slave)
spi = SPI(0, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.IN)
led = Pin(15, Pin.OUT)

while True:
    if cs.value() == 0:  
        data = spi.read(1)
        if data == b'1':
            print("Přijato: 1")
            led.toggle()
            time.sleep(0.5)
