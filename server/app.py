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
from models import User, Playlist, Song, Artist, PlaylistSong

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

    if playlist:
        db.session.delete(playlist)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Playlist has been deleted."
        }

        response = make_response(response_body, 200)
        return response

    else:
        response_body = {
            "message": "Playlist not found."
        }

        response = make_response(response_body, 404)
        return response

@app.route('/playlists', methods=['POST'])
def create_playlist():
    new_playlist = Playlist(
        name=request.json.get("name"),
        description=request.json.get("description"),
        user_id=request.json.get("user_id")
    )

    db.session.add(new_playlist)
    db.session.commit()

    playlist_dict = new_playlist.to_dict()

    response = make_response(playlist_dict, 201)
    return response

@app.route('/playlists/<int:id>', methods=['PATCH'])
def update_playlist(id):
    updated_playlist = Playlist.query.filter(Playlist.id == id).first()
    for attr in request.json:
        setattr(updated_playlist, attr, request.json.get(attr))

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
            username=request.json.get("username"),
            email=request.json.get("email"),
            password_hash=request.json.get("password"),
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
            for attr in request.json:
                setattr(user, attr, request.json.get(attr))

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


@app.route('/songs', methods=['GET', 'POST'])
def songs():
    if request.method == 'GET':
        songs = []
        for song in Song.query.all():
            song_dict = song.to_dict()
            songs.append(song_dict)

        response = make_response(songs, 200)
        return response

    elif request.method == 'POST':
        new_song = Song(
            name=request.json.get("name"),
            duration=request.json.get("duration"),
            artist_id=request.json.get("artist_id")
        )

        db.session.all(new_song)
        db.session.commit()

        song_dict = new_song.to_dict()

        response = make_response(song_dict, 201)
        return response


@app.route('/songs/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def songs_by_id(id):
    song = Song.query.filter(Song.id == id).first()

    if song == None:
        response_body = {
            "message": "This song cannot be found. Please try again."
        }
        response = make_response(response_body, 404)
        return response

    else:
        if request.method == 'GET':
            song_dict = song.to_dict()

            response = make_response(song_dict, 200)
            return response


        elif request.method == 'PATCH':
            for attr in request.json:
                setattr(song, attr, request.json.get(attr))

            db.session.add(song)
            db.session.commit()

            song_dict = song.to_dict()

            response = make_response(song_dict, 200)
            return response

        elif request.method == 'DELETE':
            db.session.delete(song)
            db.session.commit()

            response_body = {
                "delete_successful": True,
                "message": "Song has been deleted."
            }
            response = make_response(response_body, 200)
            return response


@app.route('/artists', methods=['GET', 'POST'])
def artists():
    if request.method == 'GET':
        artists = []
        for artist in Artist.query.all():
            artist_dict = artist.to_dict()
            artists.append(artist_dict)

        response = make_response(artists, 200)
        return response

    elif request.method == 'POST':
        new_artist = Artist(
            name=request.json.get("name"),
            genre=request.json.get("genre"),
        )

        db.session.add(new_artist)
        db.session.commit()

        artist_dict = new_artist.to_dict()

        response = make_response(artist_dict, 201)
        return response


@app.route('/artists/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def artists_by_id(id):
    artist = Artist.query.filter(Artist.id == id).first()

    if artist == None:
        response_body = {
            "message": "This artist cannot be found. Please try again."
        }
        response = make_response(response_body, 404)
        return response

    else:
        if request.method == 'GET':
            artist_dict = artist.to_dict()

            response = make_response(artist_dict, 200)
            return response

        elif request.method == 'PATCH':
            for attr in request.json:
                setattr(artist, attr, request.json.get(attr))

            db.session.add(artist)
            db.session.commit()

            artist_dict = artist.to_dict()

            response = make_response(artist_dict, 200)
            return response

        elif request.method == 'DELETE':
            db.session.delete(artist)
            db.session.commit()

            response_body = {
                "delete_successful": True,
                "message": "Artist has been deleted."
            }

            response = make_response(response_body, 200)
            return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)

