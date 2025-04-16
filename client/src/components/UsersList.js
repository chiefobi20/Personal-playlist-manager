import { useOutletContext } from "react-router-dom"
import User from "./User"

function UsersList(){

    const {users} = useOutletContext()
    console.log(users)
    const userComponents = users.map(user => {
        return(<User key={user.id} user={user}/>)
    })
    return(
        <ul>{userComponents}</ul>
    )
}

export default UsersList
