import styles from './DayBlock.module.sass'
interface IDayBlock {
    dayName: string
}

const DayBlock = ({ dayName, schedule, isWeekend = false }: IDayBlock) => {
    schedule = [
        {
            number: 1,
            name: "Политэкономия (лк)",
            teacher: "Павлыш Э. В.",
            audience: "141"
        },
        {
            number: 2,
            name: "Политэкономия (лк)",
            teacher: "Павлыш Э. В.",
            audience: "141"
        },
        {
            number: 3,
            name: "Политэкономия (лк)",
            teacher: "Павлыш Э. В.",
            audience: "141"
        },
        {
            number: 4,
            name: "Политэкономия (лк)",
            teacher: "Павлыш Э. В.",
            audience: "141"
        },
        {
            number: 5,
            name: "Политэкономия (лк)",
            teacher: "Павлыш Э. В.",
            audience: "141"
        },
    ]
    let scheduleList = []
    for (let i = 0; i < 8; ++i) {
        if (schedule[i]?.number === i + 1) {
            scheduleList.push(
                <li><b>{i + 1}</b>.&nbsp;
                    <b>{schedule[i].name}</b> <br />
                    {schedule[i].teacher} <br />
                    {schedule[i].audience} <br />
                </li>
            )
        }
        else {
            scheduleList.push(
                <li><b>{i + 1}</b>.&nbsp;
                </li>
            )
        }
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