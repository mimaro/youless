
# coding=utf-8

from datetime import datetime
import os

def main():

# Messwerte einlesen
    total = 0
    with open("daten.txt", "r") as f:
        for line in f:
            num = float(line)
            total += num

    total = total / 6
    print(total)

#Datei löschen


#aktuelle Zeit abfragen
    now = datetime.now()
    dt_string = now.strftime("%Y;%m;%d;%H;%M;%S")
    print(dt_string)

 # Werte in txt File schreiben
    data_out = open("daten_sum.txt", "a")
    data_out.write(dt_string + ";" + str(total) + "\n")
    data_out.close()

    data = open("daten.txt", "w")
    data.close()

#os.remove("/home/pi/daten.txt")


if __name__ == "__main__":
    main()

