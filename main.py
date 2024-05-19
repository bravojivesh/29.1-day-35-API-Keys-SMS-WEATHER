import requests
from twilio.rest import Client

#example to directly put on the browser:
#https://api.openweathermap.org/data/2.5/weather?id=1283240&appid=3fec4128de11da9ba4eae18407bf4cc1



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

if will_rain==True:
    #print ("Bring your umbrella")
    #NEED TO UNCOMMENT THIS:client = Client(twilio_SID,twilio_token)

    message = client.messages \
        .create(
        body='This is the ship that made the Kessel Run in fourteen parsecs?',
        from_="+16315935727",
        to="+9779828026885"
    )
    print(message.status)
