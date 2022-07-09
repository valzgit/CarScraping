
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.polovniautomobili.com'
driver = webdriver.Firefox(executable_path='C:/Users/PC/ChromeDriver/geckodriver.exe')
driver.get(url)
driver.maximize_window()
driver.find_element(By.CLASS_NAME,'_ado-responsiveFooterBillboard-hover').click()
driver.find_element(By.CLASS_NAME,'js-accept-cookies').click()
element = driver.find_element(By.CLASS_NAME, 'js-webpack-homepage-next')
driver.execute_script("arguments[0].scrollIntoView();", element)
session = requests.session()
while True:
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    allCarsOnAPage = soup.find('div', class_='featuredAdsHolder')
    cars = allCarsOnAPage.findAll('section', class_='uk-width-large-1-6 uk-width-medium-1-2 uk-width-1-2 uk-padding-remove')

    for car in cars:
        link = url + car.find('a')['href']
        print("Going to link: " + link)
        car_specific_html = session.get(link ,headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
        car_page_soup = BeautifulSoup(car_specific_html.text,'lxml')

        carPrice = car_page_soup.find('span', class_='priceClassified regularPriceColor')

        if carPrice is None:
            carPrice = car_page_soup.find('span', class_='priceClassified discountedPriceColor')
        print(carPrice.text)

        sellingPlace = car_page_soup.find('div', class_='infoBox js-tutorial-contact').find('div', class_='uk-grid uk-margin-top-remove').find('div',class_='uk-width-1-2')
        print(sellingPlace.contents[0].strip())

        allCarInfo = car_page_soup.find('div', class_='classified-content')
        generalInfo = allCarInfo.find('section', class_='js_fixedContetLoad').find('div', class_='infoBox').find('div', class_='uk-grid')
        allInfoRows = generalInfo.findAll('div', class_='divider')
        for infoRow in allInfoRows:
            infoClass = infoRow.find('div', class_='uk-width-1-2')
            infoValue = infoRow.find('div', class_='uk-width-1-2 uk-text-bold')
            print(infoClass.text + " - " + infoValue.text)

        additionalInfo = allCarInfo.find('div', class_='js-tab-classified-content classified-content').find('div', class_='infoBox').find('div', class_='uk-grid js-hidden uk-margin-top')
        additionalInfoRows = additionalInfo.findAll('div', class_='divider')
        for additionalInfoRow in additionalInfoRows:
            infoClass = additionalInfoRow.find('div', class_='uk-width-1-2')
            infoValue = additionalInfoRow.find('div', class_='uk-width-1-2 uk-text-bold')
            print(infoClass.text + " - " + infoValue.text)
        print("-------------------------------------------------------")
    print("Fetching next page...............")
    driver.find_element(By.CLASS_NAME, 'js-webpack-homepage-next').click()
