

# coding=utf-8

import requests
import json
import logging

# Impulsrate definieren

def main():

    impuls = int(open("impuls.txt").read())

    # Leistungswert von youless auslesen
    req = requests.get("http://169.254.32.1/a?f=j")
    data = req.content
    decoded_data = json.loads(data)
    power = str(("{}".format(decoded_data["pwr"])))
    power_corr = str(float(power) / impuls * 1000)

    print(power_corr)
    print(impuls)

    # Werte in txt File schreiben
    data_out = []
    data_out = open("daten.txt", "a")
    data_out.write(power_corr + "\n")
    data_out.close()

    power = open("power.txt", "w")
    power.write(power_corr)
    power.close()

if __name__ == "__main__":
    main()

