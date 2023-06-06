# -*- coding: utf-8 -*-

# ------------------------------------------------------
# Dateiname: Biercounter.py
# Version: 1.0
# Funktion: Anzeigen der über zwei Taster eingelesenen gezapften Biermenge auf einem Bildschirm
# Autor: MJulian Grundmann
# Datum der letzte Änderung: 06.06.23
# ------------------------------------------------------

import RPi.GPIO as GPIO
import tkinter as tk
import time

#Variable zum Zählen der Biermenge
Biercounter = 0

#Pin-Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Input-Pin für Pilztaster zum Hochzählen
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Input-Pin für Mini-Button zum rKorrigieren nach unten

#GUI-Setup
root = tk.Tk()
root.geometry('2000x1700') #Fenstergröße
root.configure(bg='purple') #Hintergrundfarbe
#root.attributes('-fullscreen', True) #Fullscreen-Modus aktivieren
root.title("Biercounter")

# Erstellen der GUI-Labels
bierausschank = tk.Label(root, text = 'Biercounter: ', bg='purple', font=('times', 250, 'bold'))
status_biermenge = tk.Label(root, text ='Bier', bg='purple', font=('times', 250, 'bold'))
liter = tk.Label(root, text = ' Liter', bg='purple', font=('times', 250, 'bold'))

#Platzieren der GUI-Labels
bierausschank.place(x=50, y=150)
status_biermenge.place(x=150, y=600)
liter.place(x=950, y=600)

#CallbackFunktion, die auf Input-Pins schaut und Label für Biermenge aktualisiert
def update_bier():
    global Biercounter
    if GPIO.input(23) == 0:
        Biercounter+=50
        status_biermenge["text"] = Biercounter
        time.sleep(1) #Entprellen des Tasters und Vermeidung von zu schnellem Hochzählen
               
    if GPIO.input(24) == 0:      
        if Biercounter > 0:
            Biercounter-=50
            status_biermenge["text"] = Biercounter
            time.sleep(1) #Entprellen des Tasters und Vermeidung von zu schnellem Korrigieren
             
    root.after(1, update_bier) #rekursiver Aufruf der Funktion
    
root.after(1, update_bier) #Aufruf der rekursiven update_bier-Funktion
root.mainloop()
    




