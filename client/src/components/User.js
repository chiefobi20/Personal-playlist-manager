function User({user}){
    console.log(user)
    return(
        <li>
            <p>Username: {user.username}</p>
            <p>Email: {user.email}</p>
        </li>
    )
}

export default User