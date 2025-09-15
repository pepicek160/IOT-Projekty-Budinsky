from machine import Pin
import time

led = Pin("LED", Pin.OUT)

led.value(1)
time.sleep(5) 
led.value(0)  
