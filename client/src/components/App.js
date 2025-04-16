import React, { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import NavBar from "./NavBar";


function App() {

  const [playlists, setPlaylists] = useState([])
  const [users, setUsers] = useState([])
  const [artists, setArtists] = useState([])
  const [songs, setSongs] = useState([])


  useEffect(getPlaylists, [])
  function getPlaylists() {
    fetch("/playlists")
    .then(response => response.json())
    .then(playlistsData => {
      setPlaylists(playlistsData)
    })
  }

  useEffect(getUsers, [])
  function getUsers() {
    fetch("/users")
    .then(response => response.json())
    .then(usersData => {
      setUsers(usersData)
    })
  }

  useEffect(getArtists, [])
  function getArtists() {
    fetch("/artists")
    .then(response => response.json())
    .then(artistsData => {
      setArtists(artistsData)
    })
  }

  useEffect(getSongs, [])
  function getSongs() {
    fetch("/songs")
    .then(response => response.json())
    .then(songsData => {
      setSongs(songsData)
    })
  }


  return (
    <div>
      <NavBar/>
      <h1>Welcome to Your Personal Playlist Manager!</h1>

      <Outlet context={
        {
          playlists: playlists,
          users: users,
          artists: artists,
          songs: songs
        }
      }/>
    </div>

  );

}

export default App;
