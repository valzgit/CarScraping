
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
    print(car_page_soup.prettify())
