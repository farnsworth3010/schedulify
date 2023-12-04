import requests
import time
from bs4 import BeautifulSoup
import mysql.connector
import openpyxl
import sys
import urllib3
import os
import sys
import datetime
import json

urllib3.disable_warnings()
connect = mysql.connector.connect(host="localhost", port="33060", user="schedule", password="12345678", database="schedule", auth_plugin='mysql_native_password')  # Подключение к базе данных
cursor = connect.cursor()

class colors:  # Цвета
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


firstLetters = ["R", "T", "V", "X", "Z", "AB", "AD", "AF"]
secondLetters = ["S", "U", "W", "Y", "AA",
                 "AC", "AE", "AF"]


def logTime():  # Логи
    """Время"""
    offset = datetime.timedelta(hours=3)
    tz = datetime.timezone(offset, name="Minsk")
    now = datetime.datetime.now(tz)
    return "["+now.strftime("%H:%M")+"] "

def log(color, text):
    """Лог в терминал"""
    print(logTime() + color + text + colors.ENDC)

def schedDate():
    """Вставляет в таблицу дату проверки"""
    offset = datetime.timedelta(hours=3)
    tz = datetime.timezone(offset, name="Minsk")
    now = datetime.datetime.now(tz)
    return "["+now.strftime("%d.%m.%Y %H:%M")+"] "


def getMergedCellVal(sheet, letter, num):  
    """Получает данные ячейки"""
    cell = sheet[f'{letter}{num}']
    rng = [s for s in sheet.merged_cells.ranges if cell.coordinate in s]
    return sheet.cell(rng[0].min_row, rng[0].min_col).value if len(rng) != 0 else cell.value


def checkDay(start, day_number, group_id, group_name, firstLetter, secondLetter, sheet):
    """Парсит день в таблице"""
    startpos = start
    days = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    for i in range(1, 9):  # Проверяем 8 пар
        subjectName = ""
        teacherFirstGroup = ""
        teacherSecondGroup = ""
        teacherOfBothGroups = ""
        audienceFirstGroup = ""
        audienceSecondGroup = ""
        audienceOfBothGroups = ""
        subjectFirstGroup = ""
        subjectSecondGroup = ""
        if getMergedCellVal(sheet, firstLetter, startpos) != getMergedCellVal(sheet, secondLetter, startpos):
            if getMergedCellVal(sheet, firstLetter, startpos) != None:
                subjectFirstGroup = getMergedCellVal(sheet, firstLetter, startpos)  # Первая подгруппа
            if getMergedCellVal(sheet, secondLetter, startpos) != None:
                subjectSecondGroup = getMergedCellVal(sheet, secondLetter, startpos)  # Вторая подгруппа
        else:
            if getMergedCellVal(sheet, firstLetter, startpos) != None:
                subjectName = getMergedCellVal(sheet, firstLetter, startpos)

        pos = startpos + 1  # Преподаватель (2 строка)
        if getMergedCellVal(sheet, firstLetter, pos) != getMergedCellVal(sheet, secondLetter, pos):  # Две группы
            if getMergedCellVal(sheet, firstLetter, pos) != None:
                teacherFirstGroup = getMergedCellVal(
                    sheet, firstLetter, pos)  # Первая подгруппа
            if getMergedCellVal(sheet, secondLetter, pos):
                teacherSecondGroup = getMergedCellVal(sheet, secondLetter, pos)  # Вторая подгруппа
        else:
            if getMergedCellVal(sheet, firstLetter, pos) != None:
                teacherOfBothGroups = getMergedCellVal(sheet, firstLetter, pos)  # Общий преподаватель

        pos = startpos + 2  # Аудитория (3 строка)
        if getMergedCellVal(sheet, firstLetter, pos) != getMergedCellVal(sheet, secondLetter, pos):  # Две группы
            if getMergedCellVal(sheet, firstLetter, pos) != None:
                audienceFirstGroup = getMergedCellVal(sheet, firstLetter, pos)  # Первая аудитория
            if getMergedCellVal(sheet, secondLetter, pos) != None:
                audienceSecondGroup = getMergedCellVal(sheet, secondLetter, pos)  # Вторая аудитория
        else:
            if getMergedCellVal(sheet, firstLetter, pos) != None:
                audienceOfBothGroups = getMergedCellVal(sheet, firstLetter, pos)  # Общая аудитория

        # Проверяем деление на группы
        if teacherFirstGroup or teacherSecondGroup or audienceFirstGroup or audienceSecondGroup:
            try:
                log(colors.BOLD, f"[{days[int(day_number)-1]} {subjectName} 1:{str(audienceSecondGroup)} 2:{str(audienceSecondGroup)} 1:{teacherFirstGroup} 2:{teacherSecondGroup}]")
                if subjectFirstGroup or subjectSecondGroup:
                    cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceFirstGroup) +
                                    """', '"""+group_id+"""', '"""+day_number+"""', '"""+subjectFirstGroup+"""', '1', '"""+teacherFirstGroup+"""', '"""+group_name+"""', '2', '1', '"""+schedDate()+"""');""")
                    cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceSecondGroup) +
                                    """', '"""+group_id+"""', '"""+day_number+"""', '"""+subjectSecondGroup+"""', '2', '"""+teacherSecondGroup+"""', '"""+group_name+"""', '2', '1', '"""+schedDate()+"""');""")
                else:
                    cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceFirstGroup) +
                                    """', '"""+group_id+"""', '"""+day_number+"""', '"""+subjectName+"""', '1', '"""+teacherFirstGroup+"""', '"""+group_name+"""', '2', '1', '"""+schedDate()+"""');""")
                    cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceSecondGroup) +
                                    """', '"""+group_id+"""', '"""+day_number+"""', '"""+subjectName+"""', '2', '"""+teacherSecondGroup+"""', '"""+group_name+"""', '2', '1', '"""+schedDate()+"""');""")
            except mysql.connector.Error as err:
                log(colors.FAIL, "Something went wrong: {}".format(err))
        elif teacherOfBothGroups or audienceOfBothGroups or subjectName:  # Общая пара
            try:
                cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceOfBothGroups) +
                                """', '"""+group_id+"""', '"""+day_number+"""', '"""+subjectName+"""', NULL, '"""+teacherOfBothGroups+"""', '"""+group_name+"""', '2', '1', '"""+schedDate()+"""');""")
                log(colors.BOLD, f"[{days[int(day_number)-1]} {subjectName} {str(audienceOfBothGroups)} {teacherOfBothGroups}]")
            except mysql.connector.Error as err:
                log(colors.FAIL + "Something went wrong: {}".format(err))
        connect.commit()
        startpos += 3  # Сдвигаем стартовую позицию к следующей паре
    print("\n")


def scanGroups(sheet, startfrom):
    """Сканирует названия групп"""
    log(colors.OKGREEN, "looking for groups...")
    groups = []
    for x in firstLetters:
        if getMergedCellVal(sheet, x, startfrom-2):
            groups.append(str(getMergedCellVal(sheet, x, startfrom-2)))
            log(colors.BOLD, str[groups[-1]])
    return groups


def findStartPosition(sheet):
    """Ищет стартовую строку в таблице"""
    for i in range(1, 20):
        if str(getMergedCellVal(sheet, "D", i)).find("курс") != -1:  # Ищем заголовок столбца
            log(colors.OKGREEN, "Start row was found: " + str(i + 5))
            return i + 5


def parse(filename):
    """Парсит таблицу"""
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active  # Открываем лист
    startfrom = findStartPosition(sheet)
    groups = scanGroups(sheet, startfrom)
    for i in range(0, len(groups)):
        position = startfrom
        # if (getMergedCellVal(sheet, firstLetters[i], startfrom-2)):
        print(logTime()+colors.HEADER+str(groups[i])+colors.ENDC)
        checkDay(position, "1",  str(2)+str(i), groups[i], firstLetters[i], secondLetters[i], sheet)
        position += 25
        checkDay(position, "2", str(2)+str(i), groups[i],  firstLetters[i], secondLetters[i], sheet)
        position += 25
        checkDay(position, "3", str(2)+str(i), groups[i], firstLetters[i], secondLetters[i], sheet)
        position += 25
        checkDay(position, "4", str(2)+str(i), groups[i],  firstLetters[i], secondLetters[i], sheet)
        position += 25
        checkDay(position, "5", str(2)+str(i), groups[i], firstLetters[i], secondLetters[i], sheet)
        position += 25
        checkDay(position, "6", str(2)+str(i), groups[i],  firstLetters[i], secondLetters[i], sheet)
    log(colors.OKGREEN, "Schedule was updated!")


def convertTable(filename):
    """Конвертирует таблицу из xls в xlsx для удобства работы"""
    log(colors.BOLD, filename)
    os.system("libreoffice --convert-to xlsx "+filename+" --headless")
    log(colors.OKGREEN, "Table converted from xls to xlsx...")
    parse(filename + "x")


def downloadXls(url):
    """Скачивает таблицу по ссылке"""
    try:
        r = requests.get(url, verify=False)
        open("table.xls", 'wb').write(r.content)
    except:
        log(colors.FAIL, "Error while downloading xls!")
        sys.exit()
    log(colors.OKGREEN, "Table downloaded...")
    convertTable("table.xls")

def downloadHtml(forced = False):
    """Загружает страницу"""
    url = "http://vsu.by/universitet/fakultety/matematiki-i-it/raspisanie.html"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
    data = None 
    while True:
        try:
            log(colors.WARNING, "Trying to download HTML page...")
            r = requests.get(url, verify=False, headers=headers)
            data = r.text
            open('schedule.html', 'w', encoding='utf-8').write(data)
            log(colors.OKGREEN, "Page downloaded...")
            break
        except:
            log(colors.FAIL, "Download failed, retrying after 60 seconds...")
            time.sleep(60)
    log(colors.WARNING, "Trying to parse...")
    soup = BeautifulSoup(data, 'html.parser')
    linkstart = "https://vsu.by"
    links = soup.find('table', {'class': 'table-bordered'}).find('td').find_all('a')
    for x in links:
        if x.get("href").find('занятий') != -1:
            linkstart += x.get("href")
            if forced:
                open("savedlink.txt", 'w').write(linkstart)
                log(colors.WARNING, "starting FORCED update...")
                cursor.execute("""TRUNCATE schedule""")
                downloadXls(linkstart)
            else:
                try:
                    savedlink = open("savedlink.txt").read()
                    log(colors.WARNING, "Old link was found")
                    log(colors.WARNING, "Trying to compare...")
                    if (savedlink == linkstart):
                        log(colors.OKGREEN, "Schedule is up to date :)!")
                    else:
                        open("savedlink.txt",'w').write(linkstart)
                        log(colors.WARNING, "starting update...")
                        cursor.execute("""TRUNCATE schedule""")
                        downloadXls(linkstart)
                except:
                    open("savedlink.txt",'w').write(linkstart)
                    log(colors.WARNING, "starting update...")
                    cursor.execute("""TRUNCATE schedule""")
                    downloadXls(linkstart)
            break


if len(sys.argv) > 1:
    if sys.argv[1] == "--force": downloadHtml(True)
    else: convertTable(sys.argv[1])
else:
    while True:
        downloadHtml(False)
        time.sleep(3600)