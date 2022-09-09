from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from http import  HTTPStatus

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:welcome$1234@localhost/moviesdb'
db = SQLAlchemy(app)

# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(80), unique=True, nullable = False)
#     email = db.Column(db.String(120), unique=True, nullable = False)

class user(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)

class movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    @staticmethod
    def add_movie(title, year, genre):
        new_movie = movie(title = title, year=year, genre=genre)
        db.session.add(new_movie)
        db.session.commit()

    @staticmethod
    def get_movies_id(id):
        data=movie.query.filter_by(id=id).first()
        return data

    @staticmethod
    def get_movies_delete_id(id):
        data = movie.query.filter_by(id=id).delete()
        db.session.commit()
        return data

    @staticmethod
    def update_movie(id,title,year,genre):
        updatedata = movie.query.filter_by(id=id).first()
        updatedata.title = title
        updatedata.year = year
        updatedata.genre = genre
        db.session.commit()


    @staticmethod
    def get_movies():
        data = movie.query.all()
        return data

class allmovies(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        movie.add_movie(title = data["title"], year = data["year"], genre = data["genre"])
        return jsonify({"message": "Added successfully", "status":HTTPStatus.OK})

    def get(self):
        data=movie.get_movies()
        print(data)
        movielist = []

        for moviedata in data:
            print(moviedata.title)
            dictmovie = {}
            dictmovie = {'title': moviedata.title,'year':moviedata.title, 'genre': moviedata.genre}
            movielist.append(dictmovie)
        return jsonify(movielist)

# class onemovie(Resource):
#     def get(self, movie_id):
#         data = movie.get_movies()
#
#         for movie_data in data:
#             dicmovie = {}
#             if movie_data.id == movie_id:
#                 dicmovie["title"] = movie_data.title
#                 dicmovie["year"] = movie_data.year
#                 dicmovie["genre"] = movie_data.genre
#                 return jsonify((dicmovie),HTTPStatus.OK)
#         else:
#             return jsonify({"message":"movie not in database", "status":HTTPStatus.NOT_FOUND})

class onemovie_getid(Resource): #filterby
    def get(self,id):
        dic = {}
        data = movie.get_movies_id(id)
        if data:
            dic["id"] = data.id
            dic["title"] = data.title
            dic["year"] = data.year
            dic["genre"] = data.genre
            return jsonify({"message":"movie got", "status":HTTPStatus.OK})
        else:
            return jsonify({"message":"movie not in database", "status":HTTPStatus.NOT_FOUND})

    def delete(self, id):
        data = movie.get_movies_delete_id(id)
        if data:
            return jsonify({"message":"movie deleted", "status":HTTPStatus.OK})
        else:
            return jsonify({"message":"movie not in database", "status":HTTPStatus.NOT_FOUND})

    def put(self, id):
        data = request.get_json()
        movie.update_movie(id, data["title"], data["year"], data["genre"])
        if data:
            #data.update({"id":data.get('id'), "title": data.get('title'), "year": data.get('year')})
            return jsonify({"message": "movie updated", "status": HTTPStatus.OK})
        else:
            return jsonify({"message": "id not correct", "status": HTTPStatus.NOT_FOUND})






api.add_resource(allmovies, "/movies")
#api.add_resource(onemovie, "/movies/<int:movie_id>")
api.add_resource(onemovie_getid, "/movies/<int:id>")
app.run()


#admin = user(username='admin', email='admin@example.com')
# app.run()
# from Flak_sqlalchemy_test import user
# newuser = user(username='ratnesh', email='myname@example.com')
# db.session.add(newuser)
# db.session.commit()
# user.query.all()
# user.query.filter_by(username='admin').first()
# from Flak_sqlalchemy_test import db
# from Flak_sqlalchemy_test import user

# user.query.all()


