import { useOutletContext } from "react-router-dom"
function UsersList(){
    const {users} = useOutletContext()
    console.log(users)
    return(
        <div>Account Users go here.</div>
    )
}

export default UsersList
