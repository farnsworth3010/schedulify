import { Link, Outlet } from "react-router-dom";
import styles from "./Root.module.sass";
import Footer from "../components/Footer/Footer";
import logo from "../assets/logo.png"
import DarkThemeToggle from "../components/DarkThemeToggle/DarkThemeToggle";
const Root = () => {
  return (
    <>
      <p className={styles.beta}>beta v131123</p>
      {/* <h1 className={styles.header}> */}
      <div className={styles.headerContainer}>

        <Link to={'/'}>
          <img className={styles.header} src={logo} />
        </Link>
        <DarkThemeToggle />
        {/* Schedul<span className={styles.headerColored}>ify</span> */}
        {/* </h1> */}
      </div>
      <Outlet />
      <Footer />
    </>
  );
};
export default Root;
