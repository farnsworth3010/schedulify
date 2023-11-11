import styles from "./Home.module.sass";
import { useSelector, useDispatch } from "react-redux"
import first_year_img from "../../assets/years/first_year.png";
import second_year_img from "../../assets/years/second_year.png";
import third_year_img from "../../assets/years/third_year.png";
import forth_year_img from "../../assets/years/forth_year.png";
import { Link } from "react-router-dom";
import { setGroup } from "../../store/scheduleSlice";
import { motion } from "framer-motion"
import { childVariants, routeVariants } from "../router";
const Home = () => {
  const groupNames = {
    first: [
      { name: "23ИСИТ1д", id: 0, },
      { name: "23ПИнж1д", id: 0, },
      { name: "23ПМ1д", id: 0, },
      { name: "23УИР1д", id: 0, },
      { name: "23ФИЗ1д", id: 0, },
      { name: "23ФМО1д", id: 0, },
    ],
    second: [
      { name: "22ИСИТ1д", id: 0, },
      { name: "22МИ1д", id: 0, },
      { name: "22ПИ_ВЕБ1д", id: 0, },
      { name: "22ПИ_ПОКС1д", id: 0, },
      { name: "22ПМ1д", id: 0, },
      { name: "22ПОИТ1д", id: 0, },
      { name: "22УИР1д", id: 0, },
      { name: "22ФИЗ1д", id: 0, },

    ],
    third: [
      { name: "21ИСИТ1д", id: 0, },
      { name: "21КБ1д", id: 0, },
      { name: "21ПИ_ВЕБ1д", id: 0, },
      { name: "21ПИ_ПОКС1д", id: 0, },
      { name: "21ПМ1д", id: 0, },
      { name: "21ПОИТ1д", id: 0, },
      { name: "21УИР1д", id: 0, },
    ],
    forth: [
      { name: "41", id: 0, },
      { name: "42", id: 0, },
      { name: "43", id: 0, },
      { name: "44", id: 0, },
      { name: "45", id: 0, },
      { name: "48", id: 0, },

    ]
  }
  const dispatch = useDispatch()
  const groupClick = (group_name: string) => {
    dispatch(setGroup(group_name))
  }

  return (
    <motion.div
      variants={routeVariants}
      initial="initial"
      animate="final"
      className="home component"
    >
      <div className={styles.coursesContainer}>
        <motion.div
        variants={childVariants} initial="initial" animate="final"
        className={styles.canteenBlock}>
          <Link target="_blank" className={styles.canteen} to={'https://vsu.by/'}>
            <div >
              Новости
            </div>
          </Link>
          <Link target="_blank" className={styles.canteen} to={'https://vsu.by/platnie-uslygi/menyu-stolovoj.html'}>
            <div>
              Меню столовой
            </div>
          </Link>
        </motion.div>
        <div className={styles.course}>
          <div className={styles.header}>
            <div className={styles.headerImage}>
              <img src={first_year_img} />
            </div>
            I курс
          </div>
          <div className={styles.groups}>
            {groupNames.first.map((group, index) =>
              <Link onClick={() => groupClick(group.name)} to={`/schedule/1${index}`}>
                <div className={styles.group}>
                  <h2>{group.name}</h2>
                </div>
              </Link>
            )}
          </div>
        </div>
        <div className={styles.course}>
          <div className={styles.header}>
            <div className={styles.headerImage}>
              <img src={second_year_img} />
            </div>
            II курс
          </div>
          <div className={styles.groups}>
            {groupNames.second.map((group, index) =>
              <Link onClick={() => groupClick(group.name)} to={`/schedule/2${index}`}>
                <div className={styles.group}>
                  <h2>{group.name}</h2>
                </div>
              </Link>
            )}
          </div>
        </div>
        <div className={styles.course}>
          <div className={styles.header}>
            <div className={styles.headerImage}>
              <img src={third_year_img} />
            </div>
            III курс
          </div>
          <div className={styles.groups}>
            {groupNames.third.map((group, index) =>
              <Link onClick={() => groupClick(group.name)} to={`/schedule/3${index}`}>
                <div className={styles.group}>
                  <h2>{group.name}</h2>
                </div>
              </Link>
            )}
          </div>
        </div>
        <div className={styles.course}>
          <div className={styles.header}>
            <div className={styles.headerImage}>
              <img src={forth_year_img} />
            </div>
            IV курс
          </div>
          <div className={styles.groups}>
            {groupNames.forth.map((group, index) =>
              <Link onClick={() => groupClick(group.name)} to={`/schedule/4${index}`}>
                <div className={styles.group}>
                  <h2>{group.name}</h2>
                </div>
              </Link>
            )}
          </div>
        </div>
      </div>
    </motion.div>
  );
};
export default Home;
