#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Artist, Song, Playlist

if __name__ == '__main__':

    with app.app_context():
        # Create and initialize a faker generator
        fake = Faker()

        # Delete all rows in "users" table
        User.query.delete()
        Artist.query.delete()
        Song.query.delete()
        Playlist.query.delete()

        print("Starting seed...")
        users = []
        # Seed code goes here!
        # Add some User instances to the list
        for n in range(5):
            user = User(username=fake.user_name(), email=fake.email(), password_hash=fake.password())
            users.append(user)
        # users.append(User(username="musicmeister2", email="ilovemusic@email.com", password_hash="music"))
        # users.append(User(username="music_fiend", email="iliveformusic@email.com", password_hash="ahaidjbf"))
        # users.append(User(username="harmonicmaster", email="musicdestiny@email.com", password_hash="ebube"))
        # users.append(User(username="barnacleboy", email="musicrocks@email.com", password_hash="djuaoub"))
        db.session.add_all(users)
        db.session.commit()


        # Add some Artist instances to the list
        Chris = (Artist(name="Chris Brown", genre="Hip Hop, R&B"))
        Hov = (Artist(name="Jay-Z", genre="Hip Hop"))
        Mike = (Artist(name="Michael Jackson", genre="Pop"))

        db.session.add_all([Chris, Hov, Mike])
        db.session.commit()

        songs = []
        songs.append(Song(name="You Rock My World", duration=339, artist=Mike))
        songs.append(Song(name="Dirt Off Your Shoulder", duration=239, artist=Hov))
        songs.append(Song(name="Fine China", duration=213, artist=Chris))
        songs.append(Song(name="Beat It", duration=258, artist=Mike))
        songs.append(Song(name="All I Need", duration=265, artist=Hov))

        db.session.add_all(songs)
        db.session.commit()


        print("Seeding successful!")