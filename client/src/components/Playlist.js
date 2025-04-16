import { useOutletContext } from "react-router-dom"

function Playlist({playlist}){
    const {deletePlaylist} = useOutletContext()


    function handleClick(){
        fetch(`/playlists/${playlist.id}`, {
            method: "DELETE"
        })
        .then(response => {
            if (response.ok){
                deletePlaylist(playlist.id)
            }
            else {
                alert("Error: Unable to delete playlist.")
            }
        })
    }


    return(
        <li>
            <p>Playlist number {playlist.id}</p>
            <p>Name: {playlist.name}</p>
            <p>Description: {playlist.description}</p>
            <button onClick={handleClick}>Delete Playlist #{playlist.id}</button>
        </li>
    )
}

export default Playlist