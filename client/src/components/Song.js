function Song({song}){
    return(
        <li>
            <p>Song number {song.id}</p>
            <p>Name: {song.name}</p>
            <p>Duration: {song.duration}s</p>
        </li>
    )
}

export default Song