import { createBrowserRouter } from "react-router-dom";
import Root from "./Root";
import Home from "./Home/Home";
import Error from "./Error/Error";
import Schedule from "./Schedule/Schedule";
import About from "./About/About";

export const childVariants = {
  initial: {
    opacity: 0,
    y: "25px",
  },
  final: {
    opacity: 1,
    y: "0px",
    transition: {
      duration: 0.2,
      delay: 0.15,
    },
  },
};
export const routeVariants = {
  initial: {
    y: "50px",
    opacity: 0
  },
  final: {
    y: "0px",
    opacity: 1,
    transition: {
      type: "spring",
      mass: 0.4,
    },
  },
};
const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <Error />,
    children: [
      {
        path: "/",
        element: <Home />
      },
      {
        path: "/schedule/:id",
        element: <Schedule />
      },
      {
        path: '/about',
        element: <About />
      }
    ]
  },
]);

export default router;
