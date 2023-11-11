import { Link, Outlet } from "react-router-dom";
import styles from "./Root.module.sass";
import Footer from "../components/Footer/Footer";
import logo from "../assets/logo.png"
const Root = () => {
  return (
    <>
      <Link to={'/'}>
        {/* <h1 className={styles.header}> */}
          <img className={styles.header} src={logo}/>
          {/* Schedul<span className={styles.headerColored}>ify</span> */}
        {/* </h1> */}
      </Link>
      <Outlet />
      <Footer />
    </>
  );
};
export default Root;
