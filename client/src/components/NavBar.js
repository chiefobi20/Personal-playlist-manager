import { NavLink } from "react-router-dom"

function NavBar(){
    return <nav>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/users">Users</NavLink>
        <NavLink to="/artists">Artists</NavLink>
        <NavLink to="/songs">Songs</NavLink>
        <NavLink to="/about">About</NavLink>
        <NavLink to="/create_playlist">Create Playlist</NavLink>
    </nav>
}

export default NavBar