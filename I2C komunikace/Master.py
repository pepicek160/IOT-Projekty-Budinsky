from machine import Pin, UART
import time

uart = UART(0, tx=Pin(0), rx=Pin(1), baudrate=9600)
button = Pin(20, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        uart.write(b'1')   # pošli 1 každých 10ms
    time.sleep(0.01)
