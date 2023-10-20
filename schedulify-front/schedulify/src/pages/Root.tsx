import { Link, Outlet } from "react-router-dom";
import styles from "./Root.module.sass";
import Footer from "../components/Footer/Footer";

const Root = () => {
  return (
    <>
      <h1 className={styles.header}>
        Schedul<span className={styles.headerColored}>ify</span>
      </h1>
      <Outlet />
      <Footer/>
    </>
  );
};
export default Root;
