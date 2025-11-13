import tkinter as tk
import RPi.GPIO as GPIO
 
# Nastavení GPIO
LED_PIN = 20  # GPIO pin 20 (pin 38)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # LED zhasnuta na startu
 
def rozsvit():
    GPIO.output(LED_PIN, GPIO.HIGH)  # Rozsvítit LED
    root.update()  # Obnovit GUI
 
def zhasni():
    GPIO.output(LED_PIN, GPIO.LOW)  # Zhasnout LED
    root.update()  # Obnovit GUI
 
# Vytvoření hlavního okna
root = tk.Tk()
root.title("Ovládání LED na GPIO20")
root.geometry("300x150")
 
# Tlačítka
button_on = tk.Button(root, text="Rozsvítit", command=rozsvit, bg="green", fg="white", height=3, width=12)
button_on.pack(pady=10)
 
button_off = tk.Button(root, text="Zhasnout", command=zhasni, bg="red", fg="white", height=3, width=12)
button_off.pack(pady=10)
 
# Funkce pro správné ukončení GPIO při zavření okna
def on_closing():
    GPIO.cleanup()
    root.destroy()
 
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()