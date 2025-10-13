from machine import Pin, UART
import time

# Nastavení LED a tlačítka
led = Pin("LED", Pin.OUT)  # interní LED
button = Pin(14, Pin.IN, Pin.PULL_UP)  # tlačítko na GP14

# UART komunikace (UART0: TX=GP0, RX=GP1)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    # Pokud je tlačítko stisknuto, pošli signál
    if not button.value():
        uart.write('1')
        time.sleep(0.2)  # debounce

    # Pokud přijde zpráva, rozsvítí LED
    if uart.any():
        msg = uart.read()
        if b'1' in msg:
            led.toggle()