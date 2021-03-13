#!/usr/bin/env python
# coding=utf-8

from Tkinter import * #für python
#from tkinter import * #für pyhton3
import delete
import cronjob
import crontab_del
import threading
import time

root = Tk() # Fenster erstellen
root.wm_title("Strommessung") # Fenster Titel
root.config(background = "#a2e200") # Hintergrundfarbe des Fensters

# Hier kommen die Elemente hin

# ---------------- Erstelle linkes Frame ------------------
#leftFrame = Frame(root, width=200, height=400) # Frame initialisieren
#leftFrame.grid(row=0, column=0, padx=50, pady=50) # Relative Position und Seitenabstand (padding) angeben

#leftLabel1 = Label(leftFrame, text=youless.main(power_corr))
#leftLabel1.grid(row=0, column=0, padx=10, pady=3)


#Logo einfügen
#imageEx = PhotoImage(file = '200x200')
#Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=3)

# ---------------- Erstelle rechtes Frame ---------------

rightFrame = Frame(root, width=400, height=400)
rightFrame.grid(row=0, column=1, padx=10, pady=3)

# Eingabefeld für Impulswert
#Buttons erstellen
buttonFrame = Frame(rightFrame)
buttonFrame.grid(row=1, column=0, padx=10, pady=3)

L0 = Label(buttonFrame, text="Aktuelle Leistung:")
L0.grid(row=0, column=0, padx=10, pady=3)

L1 = Label(buttonFrame, text= str('0') + " W")
L1.config(text = "0 W")
L1.grid(row=0, column=1, padx=10, pady=3)

def power():
    threading.Timer(10,power).start()
    power_p = str(open("power.txt").read())
    L1.config(text= str(power_p) + " W")
    print(power_p)
    return power_p

power_p = power()

L2 = Label(buttonFrame, text="Impulswert")
L2.grid(row=1, column=0, padx=10, pady=3)

E1 = Entry(buttonFrame, width=10)
E1.grid(row=1, column=1, padx=10, pady=3)

B1 = Button(buttonFrame, text="Messung starten", bg="#a2e200", width=15, command=cronjob.main)
B1.grid(row=2, column=0, padx=10, pady=3)

B2 = Button(buttonFrame, text="Messung stoppen", bg="#a2e200", width=15, command=crontab_del.main)
B2.grid(row=2, column=1, padx=10, pady=3)

B3 = Button(buttonFrame, text="Messdaten löschen", bg="#FF0000", width=15, command=delete.main)
B3.grid(row=3, column=0, padx=10, pady=3)

def impuls():
    imp = E1.get()
    imp_def = open("impuls.txt", "w")
    imp_def.write(imp)
    imp_def.close()

B4 = Button(buttonFrame, text="Impulswert definieren", bg="#FF0000", width=15, command=impuls)
B4.grid(row=3, column=1, padx=10, pady=3)

root.mainloop() # GUI wird upgedated. Danach keine Elemente setzen




