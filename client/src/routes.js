import App from "./components/App";
import ErrorPage from "./components/ErrorPage";
import PlaylistsList from "./components/PlaylistsList";
import UsersList from "./components/UsersList";
import About from "./components/About";
import ArtistsList from "./components/ArtistsList";
import SongsList from "./components/SongsList";

const routes = [
    {
        path: "/",
        element: <App/>,
        errorElement: <ErrorPage/>,
        children: [
            {
                path: "/",
                element: <PlaylistsList/>
            },
            {
                path: "/users",
                element: <UsersList/>
            },
            {
                path: "/about",
                element: <About/>
            },
            {
                path: "/artists",
                element: <ArtistsList/>
            },
            {
                path: "/songs",
                element: <SongsList/>
            }
        ]
    }
]

export default routes