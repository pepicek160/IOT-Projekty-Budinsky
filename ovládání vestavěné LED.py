from machine import Pin, UART
import time

uart = UART(0, tx=Pin(0), rx=Pin(1), baudrate=9600)
led = Pin("LED", Pin.OUT)

while True:
    if uart.any():
        data = uart.read(1)
        if data == b'1':
            led.value(1)  # rozsvítí LED
    else:
        led.value(0)      # zhasne, pokud nic nepřichází
    time.sleep(0.01)
