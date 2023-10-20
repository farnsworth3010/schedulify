import styles from "./Home.module.sass";

import first_year_img from "../../assets/years/first_year.png";
import second_year_img from "../../assets/years/second_year.png";
import third_year_img from "../../assets/years/third_year.png";
import forth_year_img from "../../assets/years/forth_year.png";
const Home = () => {
  return (
    <>
      <div className={styles.coursesContainer}>
        <div className={styles.course}>
          <div className={styles.header}>
            <div className={styles.headerImage}>
              <img src={first_year_img} />
            </div>
            I курс
          </div>
          <div className={styles.groups}>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
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
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
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
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
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
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
            <div className={styles.group}>
              <h2>23ПОИТ1д</h2>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
export default Home;
