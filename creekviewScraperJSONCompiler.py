import requests, bs4, openpyxl, time, pyperclip, pyautogui
from openpyxl import Workbook

pyautogui.PAUSE = 0.4
pyautogui.FAILSAFE = True

site = requests.get('https://cherokeek12.net/creekviewhs/faculty-staff/')
site.raise_for_status()

soupSite = bs4.BeautifulSoup(site.text, "html.parser")

names = [element.get_text() for element in soupSite.select('td[class="column-1"]')]
department = [element.get_text() for element in soupSite.select('td[class="column-2"]')]
position = [element.get_text() for element in soupSite.select('td[class="column-3"]')]
email = [element.get_text() for element in soupSite.select('td[class="column-4"]')]

#creating master list
number = int(0)
master = []

for i in range (0, len(names)):
    master.append(names[number])
    master.append(department[number])
    master.append(position[number])
    master.append(email[number])
    number = (int(number) + 1)

#making first names list
allFirstNames = []
value = int(0)

for i in range (0, len(names)):
    head, sep, tail = names[value].partition(', ')
    allFirstNames.append(tail)
    value = value+1
    
allFirstNames = [element.lower() for element in allFirstNames]

#making last names list
allLastNames = []
secondValue = int(0)

for i in range (0, len(names)):
    head, sep, tail = names[secondValue].partition(', ')
    allLastNames.append(head)
    secondValue = secondValue+1
    
allLastNames = [element.lower() for element in allLastNames]

#making title for each person, in a list
titles = []
thirdValue = int(0)

for i in range (0, len(names)):
    title = str('a '+ position[thirdValue] + ' in the ' + department[thirdValue] + ' department at Creekview High School.')
    titles.append(title)
    thirdValue = thirdValue+1


#making a sayEmail variable
sayEmail = []
fourthValue = int(0)

for i in range (0, len(email)):
    head, sep, tail = email[fourthValue].partition('.ga')
    newEmail = str(head + '.G A.U S')
    sayEmail.append(newEmail)
    fourthValue = fourthValue+1
    

#making the json data
json = []
fifthValue = int(0)

for i in range (0, len(names)):
    #{firstName:"dave",lastName:"isbitski",title:"Chief Alexa evangelist",github:"disbitski",saygithub:"d, isbitski"}
    jsonValue= ('{firstName:"'+allFirstNames[fifthValue]+'",lastName:"'+allLastNames[fifthValue]+'",title:"'+titles[fifthValue]+'",email:"'+email[fifthValue]+'",sayemail:"'+sayEmail[fifthValue]+'",department:"'+department[fifthValue]+'",saydepartment:"'+department[fifthValue]+'",position:"'+position[fifthValue]+'",sayposition:"'+position[fifthValue]+'",cityName:"canton",twitter:"not in the directory",saytwitter:"not in the directory",github:"not in the directory",saygithub:"not in the directory",linkedin:"not in the directory",saylinkedin:"not in the directory",joinDate:"forever ago",gender:"m"}')
    json.append(jsonValue)
    fifthValue = fifthValue+1

#note: cut out cityName, twitter, sayTwitter, github, saygithub, linkedin, sayLinkedin, joindate, gender
#changed github to EMAIL, and say github to sayEmail

finalNumber = int(0)
for i in range (0, len(json)):
    print(json[finalNumber] + ',')
    finalNumber = finalNumber+1

'''
#copies and pastes all names into the intents box
loop = int(0)

for i in range (0, len(allLastNames)):
    pyperclip.copy(allLastNames[loop])
    pyautogui.click(670, 336)
    pyautogui.hotkey('command', 'v')
    pyautogui.press('enter')
    loop = loop+1
'''    
