import React from "react";
import ReactDOM from "react-dom/client";
import "./index.sass";
import { RouterProvider } from "react-router-dom";
import router from "./pages/router.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);
