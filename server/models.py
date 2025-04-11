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
    def __repr__(self):
        return f"<User {self.id}, {self.username}, {self.email}>"

class Playlist(db.Model, SerializerMixin):
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

# Add Playlist realationship
    playlist_songs = db.relationship("PlaylistSong", back_populates="playlists", cascade="all")
    user = db.relationship("User", back_populates="playlists", cascade="all")
# Add serialization rules
    serialize_rules = ("-playlist_songs",)

# Add validation
    @validates("name")
    def validates_name(self, key, value):
        if (value == None) or (value == ""):
            return (f"Playlist #{self.id}")
        pass

        # if (not isinstance(value,str)) or (not (3 <= len(value) <=100)):
        #     raise ValueError("Username must be between 3 and 100 characters")
        # else:
        #     return (f"Playlist #{self.id}")

    @validates("description")
    def validates_description(self, key, value):
        if (not isinstance(value,str)) or (len(value) >= 401):
            raise ValueError("Max characters for description reached!")
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
    playlist_songs = db.relationship("PlaylistSong", back_populates="songs", cascade="all")
    artist = db.relationship("Artist", back_populates="songs", cascade="all")


# Add serialization rules
    serialize_rules = ("-playlist_songs", )

    def __repr__(self):
        return f"<Song {self.id}: {self.name}, {self.duration}>"

# Add validation


class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)

# Add Artist Relationships
    songs = db.relationship("Song", back_populates="artist")

# Add serialization rules
    serialize_rules = ("-songs.artist",)

# Add validation


class PlaylistSong(db.Model, SerializerMixin):
    __tablename__ = "playlist_songs"

    id = db.Column(db.Integer, primary_key=True)

    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"))
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))

# Add relationships
    playlists = db.relationship("Playlist", back_populates = "playlist_songs")
    songs = db.relationship("Song", back_populates = "playlist_songs")

# Add serialization rules
    serialize_rules = ("-playlist.playlist_songs", "song.playlist_songs")


# Add validation

