import Alarm from '../../components/Alarm/Alarm'
import DayBlock from '../../components/DayBlock/DayBlock'
import styles from './Schedule.module.sass'

const Schedule = () => {
    let Days = []
    const dayNames = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    for (let i = 0; i < 7; ++i) {
        if (i < 5) Days.push(<DayBlock dayName={dayNames[i]} />)
        else Days.push(<DayBlock isWeekend={true} dayName={dayNames[i]} />)
        
    }
    return <>
        <Alarm />
        {Days}
    </>
}
export default Schedule