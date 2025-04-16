import { useOutletContext } from "react-router-dom"
import Artist from "./Artist"


function ArtistsList(){

    const {artists} = useOutletContext()
    const artistComponents = artists.map(artist => {
        return(<Artist key={artist.id} artist={artist}/>)
    })

    return <ul>{artistComponents}</ul>
}

export default ArtistsList