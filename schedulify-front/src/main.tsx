import React from "react";
import ReactDOM from "react-dom/client";
import "./index.sass";
import { RouterProvider } from "react-router-dom";
import { Provider } from "react-redux/es/exports";
import router from "./pages/router.tsx";
import { store } from "./store/store.tsx";
import { AnimatePresence } from "framer-motion";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <Provider store={store}>
      <AnimatePresence>
        <RouterProvider router={router} />
      </AnimatePresence>
    </Provider>
  </React.StrictMode>
);
