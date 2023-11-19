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
                {
                    lesson.length > 1 ? // separated 
                        <div>
                            {(lesson[0]?.subject || lesson[0]?.audience || lesson[0]?.teacher) && <div className={styles.subgroupBlock}>
                                <>

                                    <>{i + 1}</>.&nbsp;
                                    Группа 1: </>
                                {lesson[0]?.subject && <span><b>{lesson[0].subject}</b></span>}
                                {lesson[0]?.teacher && <span>{lesson[0].teacher}</span>}
                                {lesson[0]?.audience && <span>{lesson[0].audience}</span>}
                            </div>
                            }
                            {(lesson[1]?.subject || lesson[1]?.audience || lesson[1]?.teacher) && <div className={styles.subgroupBlock}>

                                <>
                                
                                    {!lesson[0]?.subject && <>{i + 1}.&nbsp;</>}
                                
                                Группа 2: </>
                                {lesson[1]?.subject && <span><b>{lesson[1].subject}</b></span>}
                                {lesson[1]?.teacher && <span>{lesson[1].teacher}</span>}
                                {lesson[1]?.audience && <span>{lesson[1].audience}</span>}
                            </div>
                            }
                        </div> : // united 
                        <div>
                            {!lesson.length && <>{i + 1}.&nbsp;</>}
                            {lesson[0]?.subject && <span>

                                <b>{i + 1}</b>.&nbsp;
                                <b>{lesson[0].subject}</b></span>}
                            {lesson[0]?.teacher && <span>{lesson[0].teacher}</span>}
                            {lesson[0]?.audience && <span>{lesson[0].audience}</span>}
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