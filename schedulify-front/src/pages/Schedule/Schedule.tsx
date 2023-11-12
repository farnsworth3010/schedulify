import { useParams } from 'react-router-dom'
import Alarm from '../../components/Alarm/Alarm'
import DayBlock from '../../components/DayBlock/DayBlock'
import { useGetScheduleQuery } from '../../store/api'
import styles from './Schedule.module.sass'
import { useSelector } from "react-redux"
import { routeVariants } from '../router'
import { motion } from "framer-motion"
const Schedule = () => {
    const { id } = useParams()
    const info = useSelector((state) => state.schedule)
    const { data, isSuccess } = useGetScheduleQuery(id)
    console.log(data)
    let Days = []
    const dayNames = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if (isSuccess) {
        for (let i = 0; i < 7; ++i) {
            if (i < 5) {
                Days.push(<DayBlock key={i} schedule={data.filter((el) => el.day_number == i + 1)} dayName={dayNames[i]} />)
            }
            else {
                Days.push(<DayBlock key={i} schedule={data.filter((el) => el.day_number == i + 1)} isWeekend={true} dayName={dayNames[i]} />)
            }

        }
    }
    return (
        <motion.div
            variants={routeVariants}
            initial="initial"
            animate="final"
            className="home component"
        >
            <div className={styles.info}>
                Группа: {info.currentGroup}
            </div>
            <h1 className={styles.blockHeader}>Звонки</h1>
            {/* <div className={styles.daysContainer}> */}
            <Alarm />
            {/* {currentDay} */}
            {/* </div> */}
            <h1 className={styles.blockHeader}>Расписание на неделю</h1>
            <div className={styles.daysContainer}>

            {Days}
            </div>
        </motion.div>)
}
export default Schedule