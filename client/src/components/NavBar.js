import { NavLink } from "react-router-dom"

function NavBar(){
    return <nav>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/users">Users</NavLink>
        <NavLink to="/artists">Artists</NavLink>
        <NavLink to="/songs">Songs</NavLink>
        <NavLink to="/about">About</NavLink>
    </nav>
}

export default NavBar