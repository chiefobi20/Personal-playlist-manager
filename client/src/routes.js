import App from "./components/App";
import ErrorPage from "./components/ErrorPage";
import PlaylistsList from "./components/PlaylistsList";

const routes = [
    {
        path: "/",
        element: <App/>,
        errorElement: <ErrorPage/>,
        children: [
            {
                path: "/",
                element: <PlaylistsList/>
            }
        ]
    }
]

export default routes