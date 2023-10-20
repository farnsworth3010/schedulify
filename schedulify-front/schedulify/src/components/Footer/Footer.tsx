import { Link } from 'react-router-dom';
import styles from './Footer.module.sass'
const Footer = () => {
    return (
        <footer className={styles.footer}>
            <Link to={"/about"}>О проекте</Link>
        </footer>
    )
};
export default Footer;
