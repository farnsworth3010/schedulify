import { routeVariants } from '../router'
import styles from './About.module.sass'
import { motion } from "framer-motion"
const About = () => {
    return (
        <motion.div
            variants={routeVariants}
            initial="initial"
            animate="final"
            className="home component"
        >
            <div className={styles.aboutBlock}>
                <h3>О проекте</h3>
                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Reiciendis nesciunt laudantium eius ullam reprehenderit vitae voluptatum repudiandae sed maxime sit aut a accusamus animi est sequi sint, voluptas natus unde possimus mollitia iure amet qui non. Officia, culpa. Est praesentium quidem alias mollitia obcaecati in libero similique aperiam beatae, dolorem quam voluptatum, animi natus ducimus, sequi suscipit possimus. Et magnam quisquam nihil inventore quaerat dolor illo? Labore amet, earum reiciendis mollitia explicabo officiis error doloremque distinctio praesentium, harum veniam placeat illo sapiente omnis nemo, esse sit ad sed expedita ab repellat? Fuga voluptate, quo obcaecati inventore repellat dolorem et sed.</p>
            </div>
        </motion.div>
    )
}
export default About