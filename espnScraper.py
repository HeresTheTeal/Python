import requests, bs4, openpyxl, time, pyautogui, pyperclip
from openpyxl import Workbook

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

site = requests.get('http://www.espn.com/college-football/team/roster/_/id/61/georgia-bulldogs')
site.raise_for_status()

#define site as BS
soupSite = bs4.BeautifulSoup(site.text, "html.parser")


data = [element.get_text() for element in soupSite.select('td')]

#delete first var
del data[0:8]

#make lists of values
number = int(0)
numberPlayer = []
for i in range (0, len(data), 7):
    numberPlayer.append(data[number])
    number +=7
    
number = int(1)
names = []
for i in range (1, len(data), 7):
    names.append(data[number])
    number +=7

number = int(2)
position = []
for i in range (2, len(data), 7):
    position.append(data[number])
    number +=7

number = int(3)
height = []
for i in range (3, len(data), 7):
    height.append(data[number])
    number +=7

number = int(4)
weight = []
for i in range (4, len(data), 7):
    weight.append(data[number])
    number +=7

number = int(5)
classPlayer = []
for i in range (5, len(data), 7):
    classPlayer.append(data[number])
    number +=7

number = int(6)
hometown = []
for i in range (6, len(data), 7):
    hometown.append(data[number])
    number +=7

#making first names list
allFirstNames = []
value = int(0)

for i in range (0, len(names)):
    head, sep, tail = names[value].partition(' ')
    allFirstNames.append(head)
    value += 1
allFirstNames = [element.lower() for element in allFirstNames]

#making last names list
allLastNames = []
value = int(0)

for i in range (0, len(names)):
    head, sep, tail = names[value].partition(' ')
    allLastNames.append(tail)
    value += 1
allLastNames = [element.lower() for element in allLastNames]

#position replacements
value = int(0)
for i in range (0, len(position)):
    if position[value]=='RB':
        position[value]='Running Back'
    if position[value]=='DL':
        position[value]='Defensive Lineman'
    if position[value]=='OL':
        position[value]='Offensive Lineman'
    if position[value]=='DB':
        position[value]='Defensive Back'
    if position[value]=='WR':
        position[value]='Wide Receiver'
    if position[value]=='G':
        position[value]='Guard'
    #may need to replace 'placekicker' with 'place kicker'
    if position[value]=='PK':
        position[value]='Placekicker'
    if position[value]=='OT':
        position[value]='Offensive Tackle'
    if position[value]=='DT':
        position[value]='Defensive Tackle'
    #may need to add space below with "cornerback"
    if position[value]=='CB':
        position[value]='Cornerback'
    if position[value]=='NT':
        position[value]='Nose Tackle'
    if position[value]=='S':
        position[value]='Safety'
    if position[value]=='DE':
        position[value]='Defensive End'
    if position[value]=='TE':
        position[value]='Tight End'
    #may need a space below
    if position[value]=='FB':
        position[value]='Fullback'
    #may need space below
    if position[value]=='QB':
        position[value]='Quarterback'
    if position[value]=='LB':
        position[value]='Linebacker'
    if position[value]=='LS':
        position[value]='Long Snapper'
    if position[value]=='P':
        position[value]='Punter'
    value += 1

#hometown replacements
for i in range (0, len(hometown)):
    if hometown[i]=='--':
        hometown[i]='Somewhere not listed on ESPN'

#classPlayer replacements
for i in range (0, len(classPlayer)):
    if classPlayer[i]=='FR':
        classPlayer[i]='Freshman'
    if classPlayer[i]=='SO':
        classPlayer[i]='Sophomore'
    if classPlayer[i]=='JR':
        classPlayer[i]='Junior'
    if classPlayer[i]=='SR':
        classPlayer[i]='Senior'

#making sayHeight list
sayHeight = []

for i in range (0, len(height)):
    head, sep, tail = height[i].partition('-')
    if tail == '1':
        sayHeight.append(head+' feet, '+tail+' inch')
    else:
        sayHeight.append(head+' feet, '+tail+' inches')
    
#making printHeight list
printHeight = []
for i in range (0, len(height)):
    head, sep, tail = height[i].partition('-')
    printHeight.append(head+' ft. '+tail+' in.')

#making sayWeight list
sayWeight = []
for i in range (0, len(weight)):
    sayWeight.append(weight[i]+' pounds')

#making printWeight list
printWeight = []
for i in range (0, len(weight)):
    printWeight.append(weight[i]+' lbs.')

#making title list
title = []
for i in range (0, len(names)):
    title.append('number '+numberPlayer[i]+', is a '+classPlayer[i]+' '+position[i]+' for the U G A. bulldogs.')

#MAKING ACTUAL DATASET
json = []
for i in range (0, len(names)):
    json.append('{firstName:"'+allFirstNames[i]+'",lastName:"'+allLastNames[i]+'",playerNumber:"'+numberPlayer[i]+'",number:"'+numberPlayer[i]+'",saynumber:"'+numberPlayer[i]+'",title:"'+title[i]+'",position:"'+position[i]+'",sayposition:"'+position[i]+'",hometown:"'+hometown[i]+'",sayhometown:"'+hometown[i]+'","home town":"'+hometown[i]+'","sayhome town":"'+hometown[i]+'",class:"'+classPlayer[i]+'",sayclass:"'+classPlayer[i]+'",height:"'+printHeight[i]+'",sayheight:"'+sayHeight[i]+'",weight:"'+printWeight[i]+'",sayweight:"'+sayWeight[i]+'",cityName:"athens",joinDate:"forever ago",gender:"m"}')

'''
#grabs only unique names
myset = set(allLastNames)
allLastNamesSet = list(myset)

#focus on Chrome
pyautogui.doubleClick(242,860)
time.sleep(2)

#copy and paste all values
for i in range (0, len(allLastNamesSet)):
    pyperclip.copy(allLastNamesSet[i])
    pyautogui.click(557,312)
    pyautogui.hotkey('command', 'v')
    pyautogui.press('enter')
    print(allLastNamesSet[i]+',')
'''

#print command
for i in range (0, len(json)):
    print(json[i]+',')
