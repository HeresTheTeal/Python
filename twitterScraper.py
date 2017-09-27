import requests, bs4, openpyxl, time
from openpyxl import Workbook


site = requests.get('https://twitter.com/spacex')
site.raise_for_status()
# above is such bs


soupSite = bs4.BeautifulSoup(site.text, "html.parser")


firstStamps = [element.get_text() for element in soupSite.select('span[class="_timestamp js-short-timestamp js-relative-timestamp"]')]

tweets = [element.get_text() for element in soupSite.select('div[class="js-tweet-text-container"]')]
stamps = [element.get_text() for element in soupSite.select('span[class="_timestamp js-short-timestamp "]')]

number = int(0)
for i in range (0, len(firstStamps)):
    print('From '+firstStamps[number]+' - '+tweets[number])
    number += 1

print()
print('*********************** PREVIOUS DAYS *****************************')
print()

newNumber = int(0)
for i in range (len(firstStamps), len(stamps)):
    print('From '+stamps[newNumber]+' - '+tweets[number])
    number += 1
    newNumber += 1
