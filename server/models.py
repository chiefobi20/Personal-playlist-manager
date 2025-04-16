from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

from config import db

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password_hash = db.Column(db.String)

# Add User relationship
    playlists = db.relationship("Playlist", back_populates="user")

# Add serialization rules
    serialize_rules = ('-playlists.user',)

# Add validation
    @validates("username")
    def validates_username(self, key, value):
        if (not isinstance(value, str)) or (len(value) < 8):
            raise ValueError("Username must be at least 8 characters.")
        else:
            return value

    @validates("email")
    def validates_email(self, key, value):
        if (not isinstance(value, str)) or ('@' not in value):
            raise ValueError("Inclue @ for email")
        else:
            return value


    def __repr__(self):
        return f"<User {self.id}, {self.username}, {self.email}>"

class Playlist(db.Model, SerializerMixin):
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

# Add Playlist realationship
    playlist_songs = db.relationship("PlaylistSong", back_populates="playlist", cascade="all")
    user = db.relationship("User", back_populates="playlists")

# Add serialization rules
    serialize_rules = ("-playlist_songs", "-user", )

# Add validation
    @validates("name")
    def validates_name(self, key, value):
        if (not isinstance(value, str)) or (len(value) >= 101):
            raise ValueError("Max characters for description reached.")
        else:
            return value


    @validates("description")
    def validates_description(self, key, value):
        if (not isinstance(value,str)) or (len(value) >= 401):
            raise ValueError("Max characters for description reached.")
        else:
            return value

    def __repr__(self):
        return f"<Playlist {self.id}: {self.name}, {self.description}>"



class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    duration = db.Column(db.Integer) # Duration in seconds

    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))

# Add Song Relationship
    playlist_songs = db.relationship("PlaylistSong", back_populates="song", cascade="all")
    artist = db.relationship("Artist", back_populates="songs")


# Add serialization rules
    serialize_rules = ("-playlist_songs", "-artist")

# Add validations

    def __repr__(self):
        return f"<Song {self.id}: {self.name}, {self.duration} s>"



class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)

# Add Artist Relationships
    songs = db.relationship("Song", back_populates="artist", cascade="all")

# Add serialization rules
    serialize_rules = ("-songs.artist",)

# Add validations

    def __repr__(self):
        return f"<Artist {self.id}: {self.name}, {self.genre}>"


class PlaylistSong(db.Model, SerializerMixin):
    __tablename__ = "playlist_songs"

    id = db.Column(db.Integer, primary_key=True)

    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"))
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))

# Add relationships
    playlist = db.relationship("Playlist", back_populates = "playlist_songs")
    song = db.relationship("Song", back_populates = "playlist_songs")

# Add serialization rules
    serialize_rules = ("-playlist.playlist_songs", "-song.playlist_songs",)

    def __repr__(self):
        return f"<PlaylistSong {self.id}: {self.playlist_id}, {self.song_id}>"
