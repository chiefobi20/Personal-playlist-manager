import React from "react";
import "./index.css";
import { createRoot } from "react-dom/client";
import routes from "./routes";

import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter(routes)

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<RouterProvider router={router}/>);
