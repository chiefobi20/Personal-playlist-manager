import { useOutletContext } from "react-router-dom"

function PlaylistsList(){

    const {playlists} = useOutletContext()


    return(
        <ul>Playlists go here</ul>
    )
}

export default PlaylistsList