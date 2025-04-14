#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response
from flask_restful import Resource
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Playlist, Song, PlaylistSong

# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Define metadata, instantiate db
migrate = Migrate(app, db)
db.init_app(app)

# Instantiate REST API
# api = Api(app)

# Instantiate CORS
CORS(app)

# Views go here!

@app.route('/')
def index():
    return '<h1>Welcome to your Personal Playlist Manager!</h1>'

@app.route('/playlists')
def get_playlists():
    playlists = []
    for playlist in Playlist.query.all():
        playlist_dict = playlist.to_dict()
        playlists.append(playlist_dict)

    response = make_response(
        playlists, 200
    )
    return response

@app.route('/playlists/<int:id>')
def playlist_by_id(id):
    playlist = Playlist.query.filter(Playlist.id == id).first()

    if playlist:
        body = playlist.to_dict()
        status = 200
    else:
        body = {"message": f'Playlist {id} not found.'}
        status = 404

    return make_response(body, status)

@app.route('/playlists/<int:id>', methods=['DELETE'])
def delete_playlist_by_id(id):
    playlist = Playlist.query.filter(Playlist.id == id).first()

    db.session.delete(playlist)
    db.session.commit()

    response_body = {
        "delete_successful": True,
        "message": "Playlist has been deleted."
    }
    response = make_response(response_body, 200)

    return response

@app.route('/playlists', methods=['POST'])
def create_playlist():
    new_playlist = Playlist(
        name=request.form.get("name"),
        description=request.form.get("description"),
        user_id=request.form.get("user_id")
    )

    db.session.add(new_playlist)
    db.session.commit()

    playlist_dict = new_playlist.to_dict()

    response = make_response(playlist_dict, 201)
    return response

@app.route('/playlists/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def update_playlist(id):
    updated_playlist = Playlist.query.filter(Playlist.id == id).first()
    for attr in request.form:
        setattr(updated_playlist, attr, request.form.get(attr))

    db.session.add(updated_playlist)
    db.session.commit()

    playlist_dict = updated_playlist.to_dict()

    response = make_response(playlist_dict, 200)
    return response

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = []
        for user in User.query.all():
            user_dict = user.to_dict()
            users.append(user_dict)

        response = make_response(users, 200)

        return response

    elif request.method == 'POST':
        new_user = User(
            username=request.form.get("username"),
            email=request.form.get("email"),
            password_hash=request.form.get("password"),
        )

        db.session.add(new_user)
        db.session.commit()

        user_dict = new_user.to_dict()

        response = make_response(user_dict, 201)
        return response

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def user_by_id(id):
    user = User.query.filter(User.id == id).first()

    if user == None:
        response_body = {
            "message": "This account cannot be found. Please try again."
        }
        response = make_response(response_body, 404)
        return response

    else:
        if request.method == 'GET':
            user_dict = user.to_dict()

            response = make_response(user_dict, 200)
            return response

        elif request.method == 'PATCH':
            for attr in request.form:
                setattr(user, attr, request.form.get(attr))

            db.session.add(user)
            db.session.commit()

            user_dict = user.to_dict()

            response = make_response(
                user_dict, 200
            )
            return response

        elif request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()

            response_body = {
                "delete_successful": True,
                "message": "User account has been deleted."
            }
            response = make_response(response_body, 200)
            return response





if __name__ == '__main__':
    app.run(port=5555, debug=True)

