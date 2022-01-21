#!/bin/bash
# coding=utf-8

import requests
import json
import logging
import time

VZ_POST_URL = "http://vz.wiuhelmtell.ch/middleware.php/data/{}json?operation=add&value={}"
UUID = {
    "Power": "ad5c8090-3698-11ea-8ad7-7f796afef9a1"
}

IP_YOULESS = "http://156.154.187.10/a?f=j"
IMPULSRATE = 1000

def write_vals(uuid,val):
    poststring = VZ_POST_URL.format(uuid,val)
    postreq = requests.post(poststring)

def main():
    avg_pwr = 0
    
    for i in range (5): 
        # Leistungswert 1-5 von youless auslesen
        req = requests.get(IP_YOULESS)
        data = req.content
        decoded_data = json.loads(data)
        power = str(("{}".format(decoded_data["pwr"])))
        power_corr = int(float(power) / 1000 * IMPULSRATE)
        avg_pwr += power_corr
        print(power_corr)
        time.sleep(10)

    req = requests.get(IP_YOULESS)
    data = req.content
    decoded_data = json.loads(data)
    power = str(("{}".format(decoded_data["pwr"])))
    power_corr = int(float(power) / 1000 * IMPULSRATE)
    avg_pwr += power_corr
    print(power_corr)
    
    avg_pwr = avg_pwr/6
    write_vals(UUID["Power"],avg_pwr)
    print(avg_pwr)
    
if __name__ == "__main__":
    main()

