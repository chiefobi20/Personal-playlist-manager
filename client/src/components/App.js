import React, { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";


function App() {

  const [playlists, setPlaylists] = useState([])
  const [users, setUsers] = useState([])


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

  return (
    <div>
      <h1>Welcome to Your Music Playlist Manager!</h1>
      <Outlet context={
        {
          playlists: playlists,
          users: users
        }
      }/>
    </div>

  );

}

export default App;
