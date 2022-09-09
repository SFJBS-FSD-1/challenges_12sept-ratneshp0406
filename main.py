from flask import Flask, render_template

app = Flask(__name__) #creating instance of flsk

@app.route("/") #@ is decorator
def home_page():
    return render_template("home.html")


@app.route("/<name>") #@ is decorator
def user(name):
    #return f"<h1>Hello {name}</h1>"
    return render_template("home.html", myname=name) #jinja formating


@app.route("/info")
def info_page():
    return render_template("info.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")



app.run()