import json
import requests
import datetime

from flask import Flask, render_template, request
#import urllib.request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def myweather():
    if request.method == "POST":
        city = request.form["city"]
        print(city)
        api = "997ea79e1c9575bd4f087cf90e68205d"
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric"
        print(url)
        response = requests.get(url).json()
        print(response)
        if response["cod"] == 200:

       # data = json.loads(response)
            data = {"temp":response["main"]["temp"],
                    "lon":response["coord"]["lon"],
                    "lat": response["coord"]["lat"],
                    "name": response["name"],
                    "sunrise":datetime.datetime.fromtimestamp(response.get('sys')['sunrise']),
                    "sunset":datetime.datetime.fromtimestamp(response.get('sys')['sunset']),
                    "status":200}

            return render_template("home.html", data=data)
        elif response["cod"] == "404" :
            data = {"message":response["message"],"status":404}
            return render_template("home.html", data=data)
    else:
        data = None
        return render_template("home.html",data=data)




app.run()
# "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid"=997ea79e1c9575bd4f087cf90e68205d