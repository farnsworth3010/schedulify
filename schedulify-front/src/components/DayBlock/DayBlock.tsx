import styles from './DayBlock.module.sass'
interface IDayBlock {
    dayName: string
    schedule: [{
        audience: string
        course: string
        day_number: string
        faculty: string
        group_id: string
        group_name: string
        id: string
        lesson_number: string
        subgroup_id: string | null
        subject: string
        teacher: string
        upd: string
    }]
}

const DayBlock = ({ dayName, schedule, isWeekend = false }: IDayBlock) => {
    let scheduleList = []
    for (let i = 0; i < 8; ++i) {
        const lesson = schedule.filter((el) => el.lesson_number == String(i + 1))
        scheduleList.push(
            <li>
                <b>{i + 1}</b>.&nbsp;
                {lesson[0] && <div>
                    <b>{lesson[0]?.subject}</b> <br />
                    {lesson[0]?.teacher} <br />
                    {lesson[0]?.audience} <br />
                    &nbsp;  &nbsp;
                </div>
                }
                {lesson[1] &&
                    <div>
                        <b>{lesson[1]?.subject}</b> <br />
                        {lesson[1]?.teacher} <br />
                        {lesson[1]?.audience} <br />
                    </div>
                }
            </li>
        )
    }
    return (
        <div className={styles.dayBlock}>
            <h2 className={isWeekend ? styles.weekend : undefined}>{dayName}</h2>
            <ul className={styles.scheduleList}>
                {scheduleList}
            </ul>
        </div>
    )
}
export default DayBlock