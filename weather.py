import requests
import json
import pandas as pd

  

def wether():
    city = input("Введіть назву міста:")
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,"5fa1c253af1d6a4045b08f037daeacfe"))

    extracted = pd.io.json.json_normalize(response.json())
    
    print(extracted)

wether()
