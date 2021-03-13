
# coding=utf-8

import os

def main():
    #os.remove("/home/pi/daten_sum.txt")
    daten = open("daten_sum.txt", "w")
    daten.write("0")
    daten.close()
    power_p = open("power.txt", "w")
    power_p.write("0")
    power_p.close()

    print("Die Daten wurden gelöscht")

if __name__ == "__main__":
    main()








