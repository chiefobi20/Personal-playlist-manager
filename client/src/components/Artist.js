function Artist({artist}){
    return(
        <li>
            <p>Name: {artist.name}</p>
            <p>Genre: {artist.genre}</p>
        </li>
    )
}

export default Artist