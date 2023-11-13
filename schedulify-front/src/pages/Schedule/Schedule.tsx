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
    const { data, isSuccess } = useGetScheduleQuery(id)
    let Days = []
    const dayNames = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if (isSuccess) {
        let counter = 0
        for (let i = 0; i < 7; ++i) {
            let day = []
            while(data[counter]?.day_number == i + 1) {
                day.push(data[counter])
                ++counter
            }
            console.log(day)
            if (i < 5) {
                Days.push(<DayBlock key={i} schedule={day} dayName={dayNames[i]} />)
            }
            else {
                Days.push(<DayBlock key={i} schedule={day} isWeekend={true} dayName={dayNames[i]} />)
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
            <div className={`${styles.info} ${isSuccess ? undefined : styles.waitGroup}`}>
                Группа: {isSuccess && data[0].group_name}
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