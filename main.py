
from bs4 import BeautifulSoup
import requests

url = 'https://www.polovniautomobili.com'
session = requests.session()
html = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
soup = BeautifulSoup(html.text, 'lxml')

allCarsOnAPage = soup.find('div', class_='featuredAdsHolder')
cars = allCarsOnAPage.findAll('section', class_='uk-width-large-1-6 uk-width-medium-1-2 uk-width-1-2 uk-padding-remove')

for car in cars:
    link = car.find('a')['href']
    car_specific_html = session.get(url+link,headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
    car_page_soup = BeautifulSoup(car_specific_html.text,'lxml')

    allCarInfo = car_page_soup.find('div', class_='classified-content')
    realGeneralInfo = allCarInfo.find('section', class_='js_fixedContetLoad').find('div', class_='infoBox').find('div', class_='uk-grid')
    allInfoRows = realGeneralInfo.findAll('div', class_='divider')
    for infoRow in allInfoRows:
        infoClass = infoRow.find('div', class_='uk-width-1-2')
        infoValue = infoRow.find('div', class_='uk-width-1-2 uk-text-bold')
        print(infoClass.text + " - " + infoValue.text)
    print("-------------------------------------------------------")
