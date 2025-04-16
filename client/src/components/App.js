import React, { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";


function App() {

  const [playlists, setPlaylists] = useState([])


  useEffect(getPlaylists, [])

  function getPlaylists() {
    fetch("/playlists")
    .then(response => response.json())
    .then(playlistsData => {
      setPlaylists(playlistsData)
    })
  }

  return (
    <div>
      <h1>Welcome to Your Music Playlist Manager!</h1>
      <Outlet context={
        {
          playlists: playlists
        }
      }/>
    </div>

  );

}

export default App;
