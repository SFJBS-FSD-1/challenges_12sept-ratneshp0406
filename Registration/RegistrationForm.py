from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256
from flask_migrate import Migrate
#
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:welcome$1234@localhost/registrationdb'
db = SQLAlchemy(app)
app = Flask(__name__)
migrate = Migrate(app, db)
class user(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     username = db.Column(db.String(80), unique=True, nullable = False)
     password = db.Column(db.String(120), unique=True, nullable = False)

     @staticmethod
     def add_user(username, password):
         new_user = user(username=username, password=password)
         result = db.session.add(new_user)
         db.session.commit()
         return result

     @staticmethod
     def usr_check(username):
         data = user.query.filter_by(username=username).first()
         return data

#pip install flask flask-sqlalchemy passlib flask-restful

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login_page():
    if request.method == "GET":
        return render_template("Login.html")
    else:
        if request.method == "POST":
            username = request.form["username"]
            check_user=user.usr_check(username=username)
            return render_template("Login.html", usercheck=check_user)

@app.route("/Signup", methods = ["GET","POST"])
def sign_up():
    if request.method == "GET":
        return render_template("Signup.html", flagreg=False)
    else:
        if request.method =="POST":
            username = request.form['username']
            password = request.form['password']
            valid_user_check = user.usr_check(username=username)
            if valid_user_check:
                return render_template("Signup.html", existcheck=True,flagreg=True)
            else:
                adduser = user.add_user(username=username, password=password)
                return render_template("Signup.html", existcheck=True, flagreg=True)

if __name__ == "__main__":
    app.run()

##flask --app <appname.py> db init
# flask --app <appname.py>  db migrate
# flask --app <appname.py>  db upgrade

