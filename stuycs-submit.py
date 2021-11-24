# Copyright © Fall 2021 Ivan Chen
# Liscensed under MIT License
# A CLI tool to submit homework to the StuyCS homework server
# Bugs? https://github.com/anivanchen/stuycs-submit/issues

# class dictionary
p = {
  'p1': {
    'ACKERMAN, AIDEN': 'a2f408dd9b4',
    'CHAKRABORTY, SUDIPTA': 'a2eda18b2a4',
    'CHAO, ALLEN': 'ad130310f5b',
    'CHEN, ANTHONY': 'a592fcf3783',
    'CHEN, JACKY': 'ac637320f2a',
    'CHOI, JOSHUA': 'ab7d906004d',
    'DENG, ZI JUN': 'aa621872b9c',
    'ELLIOTT, DANIEL': 'ae232ce8f08',
    'HOQUE, FARZAD': 'a3fcf8a52b5',
    'JOBIN, DAVID': 'a0c9c8df4b6',
    'KARDAR, ZARIYA': 'af34c0e9bd9',
    'LEI, MADELINE': 'ab65186098d',
    'LI, CLEMENS': 'ae28d327968',
    'LIN, DAVID': 'ac0773018ea',
    'LIN, LILY': 'a2e9ea8a984',
    'NEGRON, MARCUS': 'aa63601307c',
    'RAHMAN, NAOWAL': 'a5adcde2ec3',
    'RISHA, RUKAIYA': 'ae3531f9538',
    'SASSANO, THEO': 'a7a8ce69d81',
    'SHI, VICKY': 'ab716312c1d',
    'TAN, TYLER': 'ae25c518cd8',
    'TAPADAR, MOHAMMED': 'ae415119c18',
    'TIRUCHELVAM, MADHAVI': 'ac37042ac0a',
    'TLACOPILCO, JORGE': 'a7b85cadce1',
    'WANG, MELODY': 'a2e409ff9f4',
    'WANG, RAYMOND': 'aa6428ac98c',
    'WONG, JAYNE': 'a2cbcbfc1e4',
    'XU, COLBY': 'aa61215cc2c',
    'YOM, RICHARD': 'a7b19f6e3a1',
    'ZAMAN, AHYAN': 'a843a30435e',
    'ZHANG, FIONA': 'a0e98ade626',
    'ZHENG, SOPHIA': 'a78fec79c91',
  },
  'p2': {
    'AHMED, SAIFAN': 'a1d82b09ba7',
    'BARRETT, SADIE': 'af38d3f7f59',
    'CATER, ZAMEEN': 'a1ce98c9087',
    'CHEN, IVAN': 'a7b0deacde1',
    'CHEN, WILL': 'a2e899cd694',
    'CLERIGO, ZIDANNI': 'ad14677b62b',
    'D ANGELO, VINCENT': 'a1dbf3f81f7',
    'DONG, RYAN': 'a59e8ace293',
    'HAI, DYLAN': 'a1da2bd7ae7',
    'HAQUE, SUMAMA': 'a2e8b1cd3c4',
    'KHURSHED, NOZANINI': 'aa6d0306b7c',
    'LAI, MONICA': 'ad175f5777b',
    'LEE, MARY': 'af343204469',
    'LIN, ELVIS': 'ad1bff7ba4b',
    'LIU, ERICA': 'a2e9bb34894',
    'LIU, KELLY': 'a5aedcdff73',
    'LUNA, ASHLEY': 'ac046f3ab4a',
    'METAXAS-PATRAS, JASON': 'ac03f5d2c5a',
    'NUDELMAN, BEN': 'aa616531d4c',
    'PASMAN, NOAM': 'a2fdcf8a7f4',
    'PENG, RYAN': 'a844b6453be',
    'PRASAD, MEDHA': 'ae320132a1b',
    'QIN, JASON': 'a1dac3fc387',
    'RAHN, NOAH': 'a3ecaaec6a5',
    'SEN, SHAURYA': 'a0ca2ef66d6',
    'SIDDARAMAIAH, TEJAS': 'a841474032e',
    'UDDAYAM, SHASH': 'ab74677100d',
    'VARGELCI, ALP': 'ad163051d5b',
    'YANG, JOYCE': 'a2fb8d9e8c4',
    'ZHENG, CHERYL': 'ad16e7d584b',
    'ZHOU, BRANDON': 'ac0b3f7385a',
    'ZOH, HWASA': 'ad1b567a8fb',
  },
  'p3': {
    'ALAM, MAHEEN': 'ac072f46cea',
    'CHE, ANDREW': 'a483c8eb1c2',
    'CHEN, ANA': 'a85527178ae',
    'CHOI, HEE WON': 'a0cbed0b6a6',
    'ERMISHKIN, PETR': 'ac613fca73a',
    'FERDOUSE, FIYAZ': 'ac061fc0f4a',
    'HAAS, MIA': 'a49bf8e91c2',
    'HINCHLIFFE, ALEXANDER': 'af400459919',
    'HONKANEN, JANINE': 'ac0a6672efa',
    'HUANG, HANGSHENG': 'a0d8c2b74c6',
    'JEAN BAPTISTE, ANTOINE': 'a59dcddfeb3',
    'JO, HARRY': 'ab6d87b3e9d',
    'KAUR, MUSKAAN': 'aa61664dd4c',
    'LIN, WILSON': 'ab71390501d',
    'MA, HAOKAI': 'a3fffedd4a5',
    'MIAHJE, FARHAN': 'af233561529',
    'NG, MASON': 'ab711657e7d',
    'ODONNELL, AIDAN': 'a583ad82793',
    'PAHUJA, ADITYA': 'a7af5e691b1',
    'POTIEVSKY, DANIEL': 'ad342e647eb',
    'SCANDURA, MARGAUX': 'a857620125e',
    'SERRY, LILY': 'ab643926a0d',
    'TAN, AIDEN': 'a0c6caea336',
    'TANG, KASSIDY': 'a2ede0e4614',
    'TASNIA, JEBA': 'af340052449',
    'VUONG, CARMIN': 'a7da55d05b1',
    'WALKUP, JO': 'a2e4dbf9584',
    'WANG, RAYMOND': 'aa001004b3c',
    'YANG, JUDY': 'af241344fd9',
    'YU, DESTIN': 'aa7d995010c',
    'ZHANG, KEVIN': 'af363050519',
    'ZUO, MATTHEW': 'a483ded2582',
  },
  'p6': {
    'ARKA, RAHEL': 'af384655859',
    'AU, ELWIN': 'ac13656177a',
    'AUDHY, RIASAT': 'a8413722d4e',
    'BAHUTSKI, NIKITA': 'a588bb89073',
    'BHUIYAN, MUIZZ': 'a0c9ca1dac6',
    'CHAN, KYLE': 'ae25dd76d08',
    'CHEN, JEFF': 'aa60477590c',
    'CHIN, EDMUND': 'ab708822e3d',
    'DASSER, SOPHIA': 'a5836ab97d3',
    'DENG, JONATHAN': 'ad175e5693b',
    'EMDAD, SHIFAUL': 'a1bedced2a7',
    'GAO, RACHEL': 'a7b0ede07c1',
    'HA, JUSTIN': 'a2e8adcb404',
    'HONG, JUSTIN': 'a0c92fb8026',
    'KLEM, SPENCER': 'a483769e5d2',
    'KRISHNAKUMAR, SHRUTHI': 'a4e99b4cfa2',
    'LI, SALINA': 'ad156f0a8eb',
    'LI, SAMUEL': 'a3f80089685',
    'LILLIS, BENJAMIN': 'a7adafa06c1',
    'LIN, ANDY': 'a2e4faea604',
    'MEI, JOSEPH': 'ab7c373318d',
    'NAKAJIMA-WU, AIDAN': 'ad171176e0b',
    'OTAJONOV, JALIL': 'aa638140b3c',
    'RIESS, AXEL': 'a840a293c7e',
    'SATTAROV, SEAN': 'ad177030c1b',
    'SELECTOR, NICOLAI': 'ab7d4121b8d',
    'WANG, ALICE': 'a2e48bef7b4',
    'WENG, HUI WEN': 'a4bdd88ee82',
    'WUN, JONATHAN': 'a7a8f5e9491',
    'ZAMAN, RAIHAN': 'a59eb6eaf73',
    'ZHANG, CALVIN': 'a49afe9bfb2',
    'ZOU, JUSTIN': 'a1d6828f387',
  },
  'p7': {
    'CHAN, KEVIN': 'a1d9dc09527',
    'CHAU, BRIAN': 'ae255605848',
    'CHEN, CALVIN': 'a84ea493aae',
    'CHEN, DONNY': 'a48e7eb32c2',
    'CHEN, JASON': 'a3ec9fed5f5',
    'CHEN, NIKI': 'af357d29a79',
    'CHIN, DYLAN': 'a8474155a5e',
    'GUEYE, BREHIMA': 'a4996afb172',
    'GUO, EUGENE': 'a7bb89fc6b1',
    'HOQUE, BORNO': 'aa6005a5f9c',
    'HUANG, ELAINE': 'ac0a637091a',
    'IBNAH, INTIA': 'a48cdc8f0c2',
    'JIN, ALLISON': 'a48db6bbff2',
    'KIM, HANNAH': 'a0a88cecad6',
    'LI, CARLA': 'a48f77cd1e2',
    'LIN, BARRY': 'a7ab4fca251',
    'LIN, JAY': 'ae216c44b18',
    'MAK, MATTHEW': 'a7bc9aae6e1',
    'PARK, JUNI': 'a3f8898a415',
    'QU, OWEN': 'af34d6e5819',
    'TAM, MATTHEW': 'aa61543007c',
    'TENG, JUNTAO': 'ab11537798d',
    'TOPIWALLA, YAZI': 'a2e9ef28704',
    'VESIALOU, KIRILL': 'ae246125ec8',
    'VIRASAMI, JARED': 'a59ea98d083',
    'WANG, INFINITY': 'a59e8b487a3',
    'WASSERCUG, MAYA': 'a5fb7b93f73',
    'WU, SHUO': 'ab70565c99d',
    'YE, ELAINE': 'ae244318d38',
    'YU, NICHOLAS': 'a48ebb9f3c2',
    'YUE, WILFORD': 'ab71164df5d',
    'ZHENG, DANIEL': 'a857b29593e',
    'Holmes, Mr': 'af326742f62',
  }
}


print("""
   _____ _                _____  _____       _____       _               _ _   
  / ____| |              / ____|/ ____|     / ____|     | |             (_) |  
 | (___ | |_ _   _ _   _| |    | (___ _____| (___  _   _| |__  _ __ ___  _| |_ 
  \___ \| __| | | | | | | |     \___ \______\___ \| | | | '_ \| '_ ` _ \| | __|
  ____) | |_| |_| | |_| | |____ ____) |     ____) | |_| | |_) | | | | | | | |_ 
 |_____/ \__|\__,_|\__, |\_____|_____/     |_____/ \__,_|_.__/|_| |_| |_|_|\__| by Ivan Chen
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
  teacherName = input('Teacher Name (ex. dholmes): ')
  term = input('Term (ex. fall2021): ')
  url = "http://bert.stuy.edu/{}/{}/pages.py".format(teacherName, term)
  response = requests.post(url).text
  if 'Not Found' in response:
    print('invalid name or term')
  else: break

period = 'p' + input('Period (number): ')

# get id from dictionary p
while True:
  name = input('Name (last, first): ').upper()
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
      file = input('File Name/Path: ')

      if exists(file) == False:
        print('invalid file path / file not found')
      else:
        break
    break

# submit
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
