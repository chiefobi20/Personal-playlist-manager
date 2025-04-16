#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Artist, Song, Playlist, PlaylistSong

if __name__ == '__main__':

    with app.app_context():
        # Create and initialize a faker generator
        fake = Faker()

        # Delete all rows in "users" table
        User.query.delete()
        Artist.query.delete()
        Song.query.delete()
        Playlist.query.delete()
        PlaylistSong.query.delete()

        print("Starting seed...")
        # Seed code goes here!
        # Add some User instances to the list
        user1 = (User(username="musicmeister2", email="ilovemusic@email.com", password_hash="music"))
        user2 = (User(username="music_fiend", email="iliveformusic@email.com", password_hash="ahaidjbf"))
        user3 = (User(username="harmonicmaster", email="musicdestiny@email.com", password_hash="ebube"))
        user4 = (User(username="barnacleboy", email="musicrocks@email.com", password_hash="djuaoub"))
        db.session.add_all([user1, user2, user3, user4])
        db.session.commit()


        # Add some Artist instances to the list
        Chris = (Artist(name="Chris Brown", genre="Hip Hop, R&B"))
        Hov = (Artist(name="Jay-Z", genre="Hip Hop"))
        Mike = (Artist(name="Michael Jackson", genre="Pop"))

        db.session.add_all([Chris, Hov, Mike])
        db.session.commit()

        # Add Song instances to the list
        song1 = (Song(name="You Rock My World", duration=339, artist=Mike))
        song2 = (Song(name="Dirt Off Your Shoulder", duration=239, artist=Hov))
        song3 = (Song(name="Fine China", duration=213, artist=Chris))
        song4 = (Song(name="Beat It", duration=258, artist=Mike))
        song5 = (Song(name="All I Need", duration=265, artist=Hov))

        db.session.add_all([song1, song2, song3, song4, song5])
        db.session.commit()

        # Add Playlist instance to the list
        play1 = (Playlist(name="Hip Hop Vibes", description="My tunes to listen to for when I need a little pick me up.", user=user1))
        play2 = (Playlist(name="Pop and Chill", description="For my impromptu dance sessions.", user=user1))
        play3 = (Playlist(name="Downtime", description="Tunes to help me get away from reality.", user=user2))

        db.session.add_all([play1, play2, play3])
        db.session.commit()

        # Many to many relationship between playlist and song (PlaylistSong)
        ps1 = PlaylistSong(playlist=play1, song=song1)
        ps2 = PlaylistSong(playlist=play2, song=song1)
        ps3 = PlaylistSong(playlist=play1, song=song2)
        ps4 = PlaylistSong(playlist=play1, song=song4)
        ps5 = PlaylistSong(playlist=play2, song=song3)
        playlistSongs = [ps1, ps2, ps3, ps4, ps5]

        db.session.add_all(playlistSongs)
        db.session.commit()


        print("Seeding successful!")