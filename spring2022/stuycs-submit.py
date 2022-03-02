# Copyright © Fall 2021 Ivan Chen
# Liscensed under MIT License
# A CLI tool to submit homework to the StuyCS homework server
# Bugs? https://github.com/anivanchen/stuycs-submit/issues

# class dictionary
p = {
  'p1': {
    'ACKERMAN, AIDEN': 'a7a15d88ce1',
    'AU, ELWIN': 'ac13656177a',
    'CHEN, IVAN': 'ac0b651765a',
    'CHEN, JACKY': 'ae415102d08',
    'CHOI, JOSHUA': 'a2e409f99d4',
    'DENG, JONATHAN': 'aa602921e4c',
    'DONG, RYAN': 'a48f9bdf382',
    'GICA, MISHEL': 'ad221077c1b',
    'GOODROW, ICHIRO': 'ad1616d070b',
    'HUANG, ELAINE': 'ae284152b38',
    'KALEFA, MOZEN': 'a2ebe9ae384',
    'LIN, ANDY': 'ac0a14048ea',
    'LIN, ELVIS': 'ab7d991dc2d',
    'LIN, TERRY': 'ad3136c37eb',
    'NEGRON, MARCUS': 'a3faf98a9e5',
    'ODONNELL, AIDAN': 'ad0b250af1b',
    'RISHA, RUKAIYA': 'a3e8ec248e5',
    'ROJAS-CESSA, NELLI': 'a0c933b96f6',
    'SASSANO, THEO': 'ad0264c372b',
    'SELECTOR, NICOLAI': 'a84e72128be',
    'TASNIA, JEBA': 'a48fbbe9ff2',
    'TENG, JUNTAO': 'a1bbf9dd327',
    'VETO, ADRIAN': 'aa75335583c',
    'WANG, WILLIAM': 'a592cfcdf63',
    'WENG, HUI WEN': 'a2dbbee88e4',
    'YE, ELAINE': 'a48ee9b2792',
    'ZHENG, DANIEL': 'a857b29593e',
  },
  'p2': {
    'CATER, ZAMEEN': 'a49bcd9c5d2',
    'CHAN, Kyle': 'ad16ee45e3b',
    'CHEN, CALVIN': 'a1d73d0a337',
    'CHEN, JASON': 'a1cebdcf7d7',
    'COLAK, MEHMET': 'aa64905089c',
    'DONG, FREDA': 'aa752365b7c',
    'HASAN, MD': 'ad02765a66b',
    'IBNAH, INTIA': 'a8401043c0e',
    'KARDAR, ZARIYA': 'ae25d1f8ac8',
    'KLEM, SPENCER': 'ad1aef07c4b',
    'KWAN, EMMA': 'a1cee20fba7',
    'LIU, ERICA': 'af3466e9549',
    'LO, WILLIAM': 'ac0633116ea',
    'LUNA, ASHLEY': 'a59df6a32d3',
    'MAK, MATTHEW': 'a843655191e',
    'METAXAS PATRAS, Jason': 'a847b19681e',
    'MIAHJE, FARHAN': 'a2fee8bc8f4',
    'NUDELMAN, Ben': 'a48f8bdf3a2',
    'PASMAN, NOAM': 'ad02307580b',
    'PENG, RYAN': 'a7bb49bac41',
    'PRASAD, MEDHA': 'af231023b0a',
    'QIN, JASON': 'ae253c03c78',
    'QIN, TIANLANG': 'aa15502792c',
    'QU, OWEN': 'a59e7c4f2b3',
    'RAHN, NOAH': 'a0df99df596',
    'SIDDARAMAIAH, TEJAS': 'ac05030476a',
    'TANG, KASSIDY': 'ab74797df8d',
    'TIRUCHELVAM, MADHAVI': 'a0fbc8e60c6',
    'TORREY, EVERETT': 'a59e7aaf5a3',
    'XU, COLBY': 'a48fcfb22c2',
    'ZABETAKIS, KASSIA': 'ac071e5573a',
    'ZOU, JUSTIN': 'ae297d70c78',
  },
  'p3': {
    'AHMED, SAIFAN': 'ad14e7c576b',
    'ALAM, MAHEEN': 'a8436b028ae',
    'BARUWAL, ABINASH': 'af31cc305d9',
    'CHANG, DANIEL': 'a85e7682b6e',
    'CHAO, ALLEN': 'a48a9a896c2',
    'CHAU, BRIAN': 'ad166536b7b',
    'CHIN, DYLAN': 'a48b8d99692',
    'CLERIGO, ZIDANNI': 'a0c9baa6bf6',
    'DENG, ZI JUN': 'a2ea90fa314',
    'ERMISHKIN, PETR': 'aa0759ac15c',
    'GAO, RACHEL': 'a483ded34f2',
    'HAAS, MIA': 'ac13706194a',
    'HALDER, AARON': 'a3fbac34485',
    'HUAN, ELAINE': 'a1d6b8cb2c7',
    'LEE, MARY': 'a1dadceaa87',
    'LI, YINGHAN': 'a84f212ed2e',
    'LIN, BARRY': 'a7ab4fca251',
    'LIN, DAVID': 'a3f88cfe715',
    'LIN, Jay': 'af307d55a09',
    'MODI, PRANJAL': 'ad02f0c1beb',
    'PAHUJA, ADITYA': 'a49c6d5a282',
    'POTIEVSKY, DANIEL': 'ab52480218d',
    'SERRY, LILY': 'ae316c73f58',
    'TAN, AIDEN': 'a3f5f9d9005',
    'WALKUP, Jo': 'a0c6f9db7a6',
    'WANG, INFINITY': 'a8435695a7e',
    'WANG, YURI': 'a2fdaa3c414',
    'WU, SHUO': 'ad16303affb',
    'WUN, JONATHAN': 'ae316c70d08',
    'ZHANG, CALVIN': 'aa74107515c',
    'ZHANG, FIONA': 'a0e98ade626',
    'ZHANG, JUNLING': 'a4bde6ca262',
  },
  'p6': {
    'ANANT, KAPIL': 'a84e534591e',
    'ARKA, RAHEL': 'ad1a6477a7b',
    'AUDHY, RIASAT': 'af364055a39',
    'BAHUTSKI, NIKITA': 'a588bb89073',
    'CHAN, KEVIN': 'ac0401d48fa',
    'CHEN, NIKI': 'ad175f0b85b',
    'CHOI, HEE WON': 'a8436583e2e',
    'DASSER, SOPHIA': 'ab6d845793d',
    'HA, JUSTIN': 'a8420761eae',
    'HAQUE, SUMAMA': 'ac065f23d2a',
    'HINCHLIFFE, ALEXANDER': 'ae511548808',
    'HONG, JUSTIN': 'a59c7aed573',
    'HOQUE, BORNO': 'a8422787dbe',
    'JO, HARRY': 'a583695d073',
    'KAUSHAL, DEAN': 'ac067462d3a',
    'KRISHNAKUMAR, SHRUTHI': 'a4e99b4cfa2',
    'LI, Samuel': 'af34cc45a49',
    'LILLIS, BENJAMIN': 'a7adafa06c1',
    'LIN, ZI XUAN': 'a7bfab60c81',
    'LIU, KELLY': 'ac3745466ea',
    'MEI, JOSEPH': 'a592d9ddf63',
    'OTAJONOV, JALIL': 'af36d415e69',
    'PARK, EUGENE': 'ad73e006dfb',
    'RAHMAN, NAOWAL': 'a0f898b7b96',
    'SEN, SHAURYA': 'ae24c018838',
    'STERN, CHARLES': 'a1ddae9d527',
    'VUONG, Carmin': 'af52dd58d39',
    'WANG, ALICE': 'ae284723b78',
    'XU, ZHI MING': 'ab42191090d',
    'YOM, RICHARD': 'af3917e6b29',
    'YUE, WILFORD': 'a842257ec6e',
    'ZAMAN, AHYAN': 'a7bc5cfbca1',
  },
  'p7': {
    'BARRETT, SADIE': 'ad1af1d5d7b',
    'BEYLISON, DINAH-LUBA': 'ab733842a7d',
    'CHAKRABORTY, SUDIPTA': 'a0cf83a9086',
    'CHE, ANDREW': 'ab7c3714e3d',
    'CHEN, ANTHONY': 'af385659d29',
    'CHEN, DONNY': 'a48e7eb32c2',
    'CHIN, EDMUND': 'a0cb3399586',
    'D ANGELO, VINCENT': 'ac062e25c2a',
    'ELLIOTT, DANIEL': 'ab7679bda5d',
    'FERDOUSE, FIYAZ': 'ae243de2d68',
    'GHOSH, ORUP': 'af343003929',
    'HUANG, HANGSHENG': 'a58d97e2193',
    'JIN, ALLISON': 'a8417a7733e',
    'JOBIN, DAVID': 'ac05041387a',
    'KAUR, Muskaan': 'a59e99b22b3',
    'KIM, HANNAH': 'ad75513170b',
    'LEI, MADELINE': 'a7a9d4ac541',
    'LIN, LILY': 'a7bcbfdfcd1',
    'LIN, WILSON': 'ae246c50548',
    'MA, HAOKAI': 'a7bbba990e1',
    'MAZUMDER, ARSHIA': 'a3c508dd2f5',
    'MEI, JUSTIN': 'ac07ff5386a',
    'RAYHAN, SYED': 'a8402772d4e',
    'SCANDURA, MARGAUX': 'ad02375470b',
    'TAM, MATTHEW': 'a2e9dcb88f4',
    'TOPIWALLA, Yazi': 'a3f8fe39615',
    'UDDAYAM, Shash': 'a847544233e',
    'VARGELCI, ALP': 'a7bc9afb7f1',
    'VESIALOU, KIRILL': 'ac064307cea',
    'WASSERCUG, MAYA': 'af51d1395d9',
    'ZAMAN, RAIHAN': 'a59eb6eaf73',
  }
}


print("""
   _____ _                _____  _____       _____       _               _ _   
  / ____| |              / ____|/ ____|     / ____|     | |             (_) |  
 | (___ | |_ _   _ _   _| |    | (___ _____| (___  _   _| |__  _ __ ___  _| |_ 
  \___ \| __| | | | | | | |     \___ \______\___ \| | | | '_ \| '_ ` _ \| | __|
  ____) | |_| |_| | |_| | |____ ____) |     ____) | |_| | |_) | | | | | | | |_ 
 |_____/ \__|\__,_|\__, |\_____|_____/     |_____/ \__,_|_.__/|_| |_| |_|_|\__|
                    __/ |                                                      
                   |___/                                                       
""")

# import requirements
import requests
from os.path import exists
from bs4 import BeautifulSoup
import getpass

# url

while True: 
  teacherName = "dholmes" # input('Teacher Name (ex. dholmes): ')
  term = "spring2022" # input('Term (ex. spring2022): ')
  url = "http://bert.stuy.edu/{}/{}/pages.py".format(teacherName, term)
  response = requests.post(url).text
  if 'Not Found' in response:
    print('invalid name or term')
  else: break

period = 'p' + "1" # input('Period (number): ')

# get id from dictionary p
while True:
  name = "CHEN, IVAN" # input('Name (last, first): ').upper()
  if name not in p.get(period, {}):
    print('invalid name')
  else: 
    nameOSIS = p.get(period, {}).get(name)
    student = str(nameOSIS + ';' + name)
    break

# authenticate
while True: 
  password = getpass.getpass('Password: ')
  response = requests.post(url, 
    data = {
      "classes": period,
      "students": student,
      "password": password,
      "Submit": 'Submit',
      "page": 'submit_homework2'
    }).text

  if 'Incorrect password' in response:
    print('invalid password')
  else: break

# get dynamic values
soup = BeautifulSoup(response, features='lxml')
assignments = [i['value'] for i in soup.find_all('option')]               # get homework options
id4 = [i['value'] for i in soup.find_all('input') if i['name'] == 'id4']  # get authentication id (referred to as OSIS in site)

assignmentList = ''
for i in assignments:
    assignmentList += i + ', '

# homework data input
while True: 
  print('Choose from: ' + assignmentList)
  for each in assignments:
    assignmentList + each
  assignment = input('Assignment: ')

  if assignment not in assignments:
    print('invalid assignment')
  else:
    comment = input('Comments: ')

    while True: 
      extension = input("extension: ")
      file = assignment + "." + extension # input('File Name/Path: ')

      if extension == "null":
        break
      elif exists(file) == False:
        print('invalid file path / file not found')
      else:
        break
    break

# submit
if extension == "null":
  response = requests.post(url, 
  data = {
    'page': 'store_homework',
    'classid': period,
    'id4': id4,
    'assignmentid': assignment,
    'teacher_comment': comment,
  }, files={'filecontents': "(binary)"})
else: 
  response = requests.post(url, 
    data = {
      'page': 'store_homework',
      'classid': period,
      'id4': id4,
      'assignmentid': assignment,
      'teacher_comment': comment,
    }, files={'filecontents': open(file, 'rb')})

if 'Stored homework.' in response.text:
  print('\n**Successfully stored.**\n\nYou may now verify your submission at https://bert.stuy.edu/{}/{}/pages.py/'.format(teacherName, term))
else: 
  print('\nError while storing submission. Please try again.')

print('\nThis window will automatically close in 10 seconds')

import time
time.sleep(10)
