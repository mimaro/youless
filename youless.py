

# coding=utf-8

import requests
import json
import logging


IP_YOULESS = "http://192.168.178.31/a?f=j"
IMPULSRATE = 10000

def main():

    impuls = int(open("impuls.txt").read())

    # Leistungswert von youless auslesen
    req = requests.get(IP_YOULESS)
    data = req.content
    decoded_data = json.loads(data)
    power = str(("{}".format(decoded_data["pwr"])))
    power_corr = str(float(power) / impuls * IMPULSRATE)

    print(power_corr)
    print(impuls)

if __name__ == "__main__":
    main()

