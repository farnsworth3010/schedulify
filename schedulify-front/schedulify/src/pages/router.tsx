import { createBrowserRouter } from "react-router-dom";
import Root from "./Root";
import Home from "./Home/Home";
import Error from "./Error/Error";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
    errorElement: <Error/>,
    children: [
        {
            path: "/",
            element: <Home/>
        }
    ]
  },
]);

export default router;
