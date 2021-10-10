from typing import Text
import requests
from win10toast import  ToastNotifier
import json
import time

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    #get the data about covid situation
    data = r.json()
    Text = f'confirmed cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("covid updates",Text,duration=20)
        time.sleep(1)
        #update value at every minute
update()