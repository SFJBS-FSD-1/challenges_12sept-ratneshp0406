import json
import requests
import datetime

from flask import Flask, render_template, request

import os

#import urllib.request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def mycovidinfo():
    global covidinfo
    if request.method == "POST":
        country = request.form["country"]
        print(country)
        #api = "997ea79e1c9575bd4f087cf90e68205d"
        #url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric"
        url = "https://api.covid19api.com/summary"
        print(url)
        response_json = requests.get(url).json()
        print(response_json)

        total_countries = response_json["Countries"]
        print(total_countries)
        for i in range(len(total_countries)):
            # if response_json["Countries"][i]["Country"] == country:
            if total_countries[i]["Country"] == country:
                print("Country found")
                country_stats = total_countries[i]
                covid_data = {
                    "TotalConfirmed": country_stats["TotalConfirmed"],
                    "TotalDeaths":country_stats["TotalDeaths"]}
        return render_template("covid_home.html", covidinfo=covid_data)


    else:
        return render_template("covid_home.html")
port=int(os.environ.get("PORT", 5000))

if __name__=="__main__":
    app.run(port=port)

# app.run()
