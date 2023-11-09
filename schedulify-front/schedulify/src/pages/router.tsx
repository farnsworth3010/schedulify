import { createBrowserRouter } from "react-router-dom";
import Root from "./Root";
import Home from "./Home/Home";
import Error from "./Error/Error";
import Schedule from "./Schedule/Schedule";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
    errorElement: <Error/>,
    children: [
        {
            path: "/",
            element: <Home/>
        },
        {
          path: "/schedule",
          element: <Schedule/>
        }
    ]
  },
]);

export default router;
