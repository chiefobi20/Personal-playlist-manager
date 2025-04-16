import { useOutletContext } from "react-router-dom"
import Playlist from "./Playlist"

function PlaylistsList(){

    const {playlists} = useOutletContext()
    const playlistComponents = playlists.map(playlist => {
        return(<Playlist key={playlist.id} playlist={playlist}/>)
    })

    return(
        <ul>{playlistComponents}</ul>
    )
}

export default PlaylistsList