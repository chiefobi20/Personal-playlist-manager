import { useOutletContext } from "react-router-dom"
import Song from "./Song"

function SongsList(){

    const {songs} = useOutletContext()
    const songComponents = songs.map(song => {
        return(<Song key={song.id} song={song}/>)
    })

    return(
        <ul>{songComponents}</ul>
    )
}

export default SongsList