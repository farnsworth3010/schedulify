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
connect = mysql.connector.connect(host="localhost", port="33060", user="schedule_test", password="ejoUge@5ui%ft2", database="schedule_test", auth_plugin='mysql_native_password') # Подключение к базе данных
cursor = connect.cursor()
class colors: # Цвета
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

firstLetters = ["D", "F", "H", "J", "L", "N", "P", "R", "T", "V", "X", "Z"]
secondLetters = [ "E", "G", "I", "K", "M", "O", "Q", "S", "U", "W", "Y"]

def logTime(): # Логи
    offset = datetime.timedelta(hours=3)
    tz = datetime.timezone(offset, name="Minsk")
    now = datetime.datetime.now(tz)
    return "["+now.strftime("%H:%M")+"] "

def schedDate(): # Дата проверки на сайте
    offset = datetime.timedelta(hours=3)
    tz = datetime.timezone(offset, name="Minsk")
    now = datetime.datetime.now(tz)
    return "["+now.strftime("%d.%m.%Y %H:%M")+"] "
def checkDate(): # Дата проверки на сайте
    offset = datetime.timedelta(hours=3)
    tz = datetime.timezone(offset, name="Minsk")
    now = datetime.datetime.now(tz)
    return "["+now.strftime("%H:%M")+"] "


def getMergedCellVal(sheet, cell): # Получить данные ячейки
    rng = [s for s in sheet.merged_cells.ranges if cell.coordinate in s]
    return sheet.cell(rng[0].min_row, rng[0].min_col).value if len(rng)!=0 else cell.value

def getCellVal(sheet, letter, num): # Упрощение получения данных ячейки
    return getMergedCellVal(sheet, sheet[f'{letter}{num}'])

def downloadXls(url, course, faculty = 1):
    try:
        r = requests.get(url, verify=False) # Скачиваем таблицу по полученной ссылке
        open("table"+str(course)+".xls", 'wb').write(r.content)
        print(logTime()+colors.OKGREEN+"Table downloaded..."+colors.ENDC) 
    except:
        print(logTime()+colors.FAIL+"Error while downloading xls!"+colors.ENDC)
        sys.exit()
    xlsToMysql("table"+str(course)+".xls", course, faculty)

def scanGroups(sheet, startfrom):
    groups = []
    for x in firstLetters:
        if getCellVal(sheet, x, startfrom-2):
            groups.append(str(getCellVal(sheet, x, startfrom-2)))
            print(logTime()+str(getCellVal(sheet, x, startfrom-2)))
    return groups

def xlsToMysql(filename, course, faculty):
    print(logTime()+filename)
    os.system("libreoffice --convert-to xlsx "+filename+" --headless")
    print(logTime()+colors.OKGREEN+"Table converted from xls to xlsx..."+colors.ENDC) 
    wb = openpyxl.load_workbook(filename+"x") # Открываем таблицу
    sheet = wb.active # Открываем лист
    def checkDay(start, dayname, day_number, group_id, group_name, firstLetter, secondLetter):
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
            if(getCellVal(sheet, firstLetter, startpos) != getCellVal(sheet, secondLetter, startpos)):   
                if(getCellVal(sheet, firstLetter, startpos) != None):
                    subjectFirstGroup = getCellVal(sheet, firstLetter, startpos) # Первая подгруппа
                if(getCellVal(sheet, secondLetter, startpos) != None):
                    subjectSecondGroup = getCellVal(sheet, secondLetter, startpos) # Вторая подгруппа
            else:
               if(getCellVal(sheet, firstLetter, startpos) != None):
                    subjectName = getCellVal(sheet, firstLetter, startpos)

            pos = startpos + 1 # Преподаватель (2 строка)
            if(getCellVal(sheet, firstLetter, pos) != getCellVal(sheet, secondLetter, pos)): # Две группы
                if(getCellVal(sheet, firstLetter, pos) != None):
                    teacherFirstGroup = getCellVal(sheet, firstLetter, pos) # Первая подгруппа
                if(getCellVal(sheet, secondLetter, pos)):
                    teacherSecondGroup = getCellVal(sheet, secondLetter, pos) # Вторая подгруппа
            else:
                if(getCellVal(sheet, firstLetter, pos) != None):
                    teacherOfBothGroups = getCellVal(sheet, firstLetter, pos) # Общий преподаватель
                    
            pos = startpos + 2 # Аудитория (3 строка)
            if(getCellVal(sheet, firstLetter, pos) != getCellVal(sheet, secondLetter, pos)): # Две группы
                if(getCellVal(sheet, firstLetter, pos) != None):
                    audienceFirstGroup = getCellVal(sheet, firstLetter, pos) # Первая аудитория
                if(getCellVal(sheet, secondLetter, pos) != None):
                    audienceSecondGroup = getCellVal(sheet, secondLetter, pos) # Вторая аудитория
            else:
                if(getCellVal(sheet, firstLetter, pos) != None):
                    audienceOfBothGroups = getCellVal(sheet, firstLetter, pos) # Общая аудитория

            if(teacherFirstGroup or teacherSecondGroup or audienceFirstGroup or audienceSecondGroup): # Проверяем деление на группы
                try:
                    print(logTime()+f"[{days[int(day_number)-1]} {subjectName} 1:{str(audienceSecondGroup)} 2:{str(audienceSecondGroup)} 1:{teacherFirstGroup} 2:{teacherSecondGroup}]")
                    if(subjectFirstGroup or subjectSecondGroup):
                        cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceFirstGroup)+"""', '"""+str(group_id)+"""', '"""+str(day_number)+"""', '"""+subjectFirstGroup+"""', '1', '"""+teacherFirstGroup+"""', '"""+group_name+"""', '"""+str(course)+"""', '"""+str(faculty)+"""', '"""+schedDate()+"""');""")
                        cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceSecondGroup)+"""', '"""+str(group_id)+"""', '"""+str(day_number)+"""', '"""+subjectSecondGroup+"""', '2', '"""+teacherSecondGroup+"""', '"""+group_name+"""', '"""+str(course)+"""', '"""+str(faculty)+"""', '"""+schedDate()+"""');""")
                    else:
                        cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceFirstGroup)+"""', '"""+str(group_id)+"""', '"""+str(day_number)+"""', '"""+subjectName+"""', '1', '"""+teacherFirstGroup+"""', '"""+group_name+"""', '"""+str(course)+"""', '"""+str(faculty)+"""', '"""+schedDate()+"""');""")
                        cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceSecondGroup)+"""', '"""+str(group_id)+"""', '"""+str(day_number)+"""', '"""+subjectName+"""', '2', '"""+teacherSecondGroup+"""', '"""+group_name+"""', '"""+str(course)+"""', '"""+str(faculty)+"""', '"""+schedDate()+"""');""")
                    connect.commit()
                except mysql.connector.Error as err:
                    print(logTime()+"Something went wrong: {}".format(err))
            elif(teacherOfBothGroups != "" or audienceOfBothGroups != "" or subjectName != ""): # Общая пара
                try:
                    cursor.execute("""INSERT INTO `schedule` (id, lesson_number, audience, group_id, day_number, subject, subgroup_id, teacher, group_name, course, faculty, upd) VALUES (NULL, '"""+str(i)+"""', '"""+str(audienceOfBothGroups)+"""', '"""+str(group_id)+"""', '"""+str(day_number)+"""', '"""+subjectName+"""', NULL, '"""+teacherOfBothGroups+"""', '"""+group_name+"""', '"""+str(course)+"""', '"""+str(faculty)+"""', '"""+schedDate()+"""');""")
                    print(logTime()+f"[{days[int(day_number)-1]} {subjectName} {str(audienceOfBothGroups)} {teacherOfBothGroups}]")
                    connect.commit()
                except mysql.connector.Error as err:
                    print(logTime()+"Something went wrong: {}".format(err))
            startpos = startpos+3 # Сдвигаем стартовую позицию к следующей паре
        print("\n")
    startfrom = 0 # Стартовая строка
    for i in range(1,20): 
        if(str(getCellVal(sheet, "D", i)).find("курс") != -1): # Ищем заголовок столбца
            startfrom = i+4 # Назначаем стартовую позицию (1 строка)
            print(logTime()+colors.OKGREEN+"Start row was found: "+str(startfrom)+colors.ENDC)
            break

    print(logTime()+colors.OKGREEN+"looking for groups.."+colors.ENDC)
    groups = scanGroups(sheet, startfrom)

    monday = startfrom
    tuesday = startfrom+27
    wednesday = tuesday+27
    thursday = wednesday+27
    friday = thursday+27
    saturday = friday+27

    for i in range(0, 10): # Проверяем каждый день каждой группы
        if (getCellVal(sheet, firstLetters[i], startfrom-2)):
            print(logTime()+colors.HEADER+str(groups[i])+colors.ENDC)
            checkDay(monday, "Понедельник", "1",  int(str(course)+str(i)), groups[i], firstLetters[i], secondLetters[i])
            checkDay(tuesday, "Вторник", "2", int(str(course)+str(i)), groups[i],  firstLetters[i], secondLetters[i])
            checkDay(wednesday, "Среда", "3", int(str(course)+str(i)),  groups[i], firstLetters[i], secondLetters[i])
            checkDay(thursday, "Четверг", "4", int(str(course)+str(i)), groups[i],  firstLetters[i], secondLetters[i])
            checkDay(friday, "Пятница", "5", int(str(course)+str(i)), groups[i], firstLetters[i], secondLetters[i])
            checkDay(saturday, "Суббота", "6", int(str(course)+str(i)), groups[i],  firstLetters[i], secondLetters[i])
    print(logTime()+colors.OKGREEN+"Schedule was updated!"+colors.ENDC)

def downloadHtml():
    testjson = {'lastcheck': checkDate()}
    jsonString = json.dumps(testjson, indent=4)
    open('./test.json', 'w', encoding='utf-8').write(jsonString) # Запись страницы в файл
    now = datetime.datetime.now()
    print(logTime()+colors.WARNING+"Trying to download HTML page..."+colors.ENDC)
    url = "http://vsu.by/universitet/fakultety/matematiki-i-it/raspisanie.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    gotPage = False
    data = ""
    r = ""
    while(gotPage != True):
        try:
            r = requests.get(url, verify=False, headers=headers) # Получение страницы
            data = r.text # Сохранение текста страницы
            open('schedule.html', 'w', encoding='utf-8').write(data) # Запись страницы в файл
            print(logTime()+colors.OKGREEN+"Page downloaded..."+colors.ENDC)
            gotPage = True 
        except:
            print(logTime()+colors.FAIL+"Download failed, retrying..."+colors.ENDC) 
            time.sleep(60)
    print(logTime()+colors.WARNING+"Trying to parse..."+colors.ENDC)
    # try:
    soup = BeautifulSoup(data, 'html.parser')
    linkstart = "https://vsu.by"
    links = soup.find('table', {'class': 'table-bordered'}).find('td').find_all('a') # Поиск ссылки на файл
    course = 1

    for x in links:
        if x.get("href").find('занятий') != -1:
            try:
                savedlink = open("savedlink" +str(course)+".txt").read() # Проверяем сохранена ли ссылка на прошлое
                print(logTime()+colors.WARNING+"Old link was found..."+colors.ENDC)
                print(logTime()+colors.WARNING+"Trying to compare..."+colors.ENDC)
                if(savedlink == linkstart+x.get("href")): # Сравниваем прошлое расписание с полученным
                    print(logTime()+colors.OKGREEN+"Schedule for course "+str(course)+" is up to date :)!"+colors.ENDC)
                    course = course + 1
                    continue
                else:
                    open("savedlink"+str(course)+".txt", 'w').write(linkstart+x.get("href"))
                    print(logTime()+colors.WARNING+colors.WARNING+"starting update..."+colors.ENDC)
                    cursor.execute("""DELETE FROM schedule WHERE course = """+str(course) +"""""") # Стираем базу данных :)
                    downloadXls(linkstart+x.get("href"), course, 1)
            except:
                open("savedlink"+str(course)+".txt", 'w').write(linkstart+x.get("href"))
                print(logTime()+colors.WARNING+colors.WARNING+"starting update..."+colors.ENDC)
                cursor.execute("""DELETE FROM schedule WHERE course = """+str(course) +"""""") # Стираем базу данных :)
                downloadXls(linkstart+x.get("href"), course, 1)
            course = course + 1
    

if(len(sys.argv) > 1):
    xlsToMysql(sys.argv[1], 1, 1)
else:
    while(True):
        downloadHtml()
        time.sleep(600)
