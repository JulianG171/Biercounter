# -*- coding: utf-8 -*-

# ------------------------------------------------------
# Dateiname: Biercounter.py
# Version: 1.0
# Funktion: Anzeigen der über zwei Taster eingelesenen gezapften Biermenge auf einem Bildschirm
# Autor: MJulian Grundmann
# Datum der letzte Änderung: 07.06.23
# ------------------------------------------------------

import RPi.GPIO as GPIO
import tkinter as tk
import time, csv, datetime

BIERDATEI = '/home/jgrundmann/Biermenge.txt'
FASSLOG = '/home/jgrundmann/Fasslog.csv'

#Datei für Biermenge initial mit 0 befüllen
zapfen(0, log_schreiben = False)

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
status_biermenge = tk.Label(root, text ='0', bg='purple', font=('times', 250, 'bold'))
liter = tk.Label(root, text = ' Liter', bg='purple', font=('times', 250, 'bold'))

#Platzieren der GUI-Labels
bierausschank.place(x=50, y=150)
status_biermenge.place(x=150, y=600)
liter.place(x=950, y=600)

#CallbackFunktion, die auf Input-Pins schaut und Wert in Datei sowie Label für Biermenge aktualisiert
def update_bier():
    biermenge = lese_biermenge()

    #Pilzknopp wird gedrückt -> 50L wurden gezapft
    if GPIO.input(23) == 0:
        biermenge+=50
        zapfen(biermenge)
        time.sleep(1) #Entprellen des Tasters und Vermeidung von zu schnellem Hochzählen
        
    #Miniknopp wird gedrückt, -> Wert um 50L nach unten korrigieren
    if GPIO.input(24) == 0:      
        biermenge-=50
        zapfen(biermenge)
        time.sleep(1) #Entprellen des Tasters und Vermeidung von zu schnellem Hochzählen
            
    status_biermenge["text"] = biermenge       
    root.after(1, update_bier) #rekursiver Aufruf der Funktion

def lese_biermenge():
    with open(BIERDATEI, 'r') as datei:
        biermenge = int(datei.read())
        datei.close()

    return biermenge

#Speichert die Biermenge in BIERDATEI und im FASSLOG
def zapfen(biermenge, log_schreiben = True):
    if biermenge < 0:  # Keine negativen Werte möglich
        return

    with open(BIERDATEI, 'w') as datei:
        datei.truncate(0)
        datei.write(str(biermenge))
        datei.close()

    if log_schreiben:
        jetzt = datetime.datetime.now().strftime('%Y-%m-%d %H:%i:%s')
        log_fass(jetzt, biermenge)

#Schreibt einen neuen Eintrag mit Zeit und Biermenge ins FASSLOG
def log_fass(zeit, biermenge):
    with open(FASSLOG, 'a', newline='') as datei:
        fasslog = csv.writer(datei)
        fasslog.writerow([zeit, biermenge])
        datei.close()
    
root.after(1, update_bier) #Aufruf der rekursiven update_bier-Funktion
root.mainloop()





