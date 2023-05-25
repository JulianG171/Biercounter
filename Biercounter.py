# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import RPi.GPIO as GPIO
import tkinter as tk
import time

Biercounter = 0

GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.OUT)
#GPIO.output(17, GPIO.LOW)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

root = tk.Tk()
root.geometry('2000x1700')
root.configure(bg='purple')
#root.attributes('-fullscreen', True)
root.title("Biercounter")
status_biermenge = tk.Label(root, text ='Bier', bg='purple', font=('times', 250, 'bold'))
bierausschank = tk.Label(root, text = 'Biercounter: ', bg='purple', font=('times', 250, 'bold'))
liter = tk.Label(root, text = ' Liter', bg='purple', font=('times', 250, 'bold'))
bierausschank.place(x=50, y=150)
status_biermenge.place(x=150, y=600)
liter.place(x=950, y=600)

def update_bier():
    global Biercounter
    if GPIO.input(23) == 0:
        Biercounter+=50
        status_biermenge["text"] = Biercounter
        time.sleep(1)
               
    if GPIO.input(24) == 0:      
        if Biercounter > 0:
            Biercounter-=50
            status_biermenge["text"] = Biercounter
            time.sleep(1)
             
    root.after(1, update_bier)
    
root.after(1, update_bier)
root.mainloop()
    




