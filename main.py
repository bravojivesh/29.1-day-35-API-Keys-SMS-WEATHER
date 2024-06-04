#JH: will only work if the vn variables are set correctly.

import os
import requests
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

#website: https://openweathermap.org/forecast5

url="https://api.openweathermap.org/data/2.5/forecast/"

#if you need raw value check google drive>password>sheet 6
api_key=os.environ.get("jh_api")

params={
            "lon": 85.316666,
            "lat": 27.716667,
            "appid":api_key,
            "cnt":4
        }
# the "cnt" is for how many timestamps to be included.

response = requests.get(url, params=params)
data=response.json()
data0=str(data)

#just for me: to store in a text file to read it easily.
with open('output.txt', 'a') as file:
    file.write("\n"+ data0)

print (data)
# print (data["list"][1]["main"])
# print (data["list"][1]["weather"])

will_rain=False

for per_hour in data["list"]: #loop through all hourly data
    row_with_id=per_hour["weather"]
    id_only=row_with_id[0]["id"]
    if id_only < 700:
       will_rain=True


sid=os.environ.get("jh_sid")
token=os.environ.get("jh_token")

from_phone= "+16315935727",
to_phone= "+9779828026885"

client1=Client(sid, token)

if will_rain==True:
    print ("Bring your umbrella")
    #NEED TO UNCOMMENT THIS:client = Client(twilio_SID,twilio_token)

    try:
        message = client1.messages.create(
            body="hi Jose",
            from_=from_phone,
            to=to_phone
        )
        print(f"Message sent! SID: {message.sid}")
    except TwilioRestException as e:
        print(f"Twilio error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(message.status)
