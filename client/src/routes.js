import App from "./components/App";
import ErrorPage from "./components/ErrorPage";
import PlaylistsList from "./components/PlaylistsList";
import UsersList from "./components/UsersList";

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
            }
        ]
    }
]

export default routes