function Playlist({playlist}){
    console.log(playlist)
    return(
        <li>
            <p>Playlist number {playlist.id}</p>
            <p>Name: {playlist.name}</p>
            <p>Description: {playlist.description}</p>
        </li>
    )
}

export default Playlist