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





if __name__ == '__main__':
    app.run(port=5555, debug=True)

