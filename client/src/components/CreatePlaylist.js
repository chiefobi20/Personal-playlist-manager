import React, {useState} from "react";
import ReactDOM from "react-dom"
import { useOutletContext, useNavigate } from "react-router-dom";

function CreatePlaylist() {

    const {addPlaylist} = useOutletContext()
    const navigate = useNavigate()

    const [formData, setFormData] = useState({
        name: "",
        description: "",
        user_id: "1"
    })

    function updateFormData(event){
        setFormData({
            ...formData,
            [event.target.name]: event.target.value
        })
    }

    function handleSubmit(event){
        event.preventDefault()
        const newPlaylist = {
            ...formData,
            user_id: Number(formData.user_id)
        }
        fetch("/playlists", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(newPlaylist)
        })
        .then(response => {
            if(response.ok){
                response.json().then(newPlaylist => {
                    addPlaylist(newPlaylist)
                    navigate("/")
                })
            }
        })

    }

    return(
        <>
            <h1>Create Your Custom Playlist</h1>
            <form onSubmit={handleSubmit}>
                <label>Name: </label>
                <input onChange={updateFormData} name="name" type="text" value={formData.name}/>
                <br/>
                <br/>
                <label>Description: </label>
                <input onChange={updateFormData} name="description" type="text" value={formData.description}/>
                <br/>
                <br/>
                <label>User ID: </label>
                <input onChange={updateFormData} name="user_id" type="number" value={formData.user_id}/>
                <br></br>
                <br></br>
                <input type="submit" value="Add Playlist"/>
            </form>
        </>
    )
}


export default CreatePlaylist