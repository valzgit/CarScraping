from bs4 import BeautifulSoup
import requests

from database import DatabaseInteractor

baseUrl = 'https://www.polovniautomobili.com'
first_url_part = 'https://www.polovniautomobili.com/auto-oglasi/pretraga?page='
seconds_url_part = '&sort=basic&city_distance=0&showOldNew=all&without_price=1'
session = requests.session()
database = DatabaseInteractor()
database.initConnection()
fetched_cars = 0
page = 1
set = set()
while fetched_cars < 22000:
    html = session.get(first_url_part + str(page) + seconds_url_part, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True).text
    soup = BeautifulSoup(html, 'lxml')

    cars = soup.findAll('div', class_='textContent')
    for car in cars:
        marka = None
        model = None
        cena = None
        stanje = None
        grad = None
        godiste = None
        karoserija = None
        vrsta_goriva = None
        boja = None
        kubikaza = None
        snaga_motora = None
        kilometraza = None
        menjac = None
        broj_vrata = None
        link = baseUrl + car.find('a')['href']
        if set.__contains__(link):
            print('Already visited this car: ' + link)
            continue
        else:
            set.add(link)
            print("Going to link: " + link)
        car_specific_html = session.get(link ,headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
        car_page_soup = BeautifulSoup(car_specific_html.text,'lxml')

        carPrice = car_page_soup.find('span', class_='priceClassified regularPriceColor')

        if carPrice is None:
            carPrice = car_page_soup.find('span', class_='priceClassified discountedPriceColor')
        if carPrice.text == "Po dogovoru":
            continue
        try:
            cena = int(carPrice.text.split()[0].replace('.', ''))
        except Exception as error:
            continue

        sellingPlace = car_page_soup.find('div', class_='infoBox js-tutorial-contact').find('div', class_='uk-grid uk-margin-top-remove').find('div',class_='uk-width-1-2')
        grad = sellingPlace.contents[0].strip()

        allCarInfo = car_page_soup.find('div', class_='classified-content')
        generalInfo = allCarInfo.find('section', class_='js_fixedContetLoad').find('div', class_='infoBox').find('div', class_='uk-grid')
        allInfoRows = generalInfo.findAll('div', class_='divider')
        for infoRow in allInfoRows:
            infoClass = infoRow.find('div', class_='uk-width-1-2')
            infoValue = infoRow.find('div', class_='uk-width-1-2 uk-text-bold')
            if infoClass.text == "Stanje:":
                stanje = infoValue.text
            elif infoClass.text == "Marka":
                marka = infoValue.text
            elif infoClass.text == "Model":
                model = infoValue.text
            elif infoClass.text == "Karoserija":
                karoserija = infoValue.text
            elif infoClass.text == "Gorivo":
                vrsta_goriva = infoValue.text
            elif infoClass.text == "Godište":
                godiste = int(infoValue.text.replace('.', ''))
            elif infoClass.text == "Kilometraža":
                kilometraza = int(infoValue.text.split()[0].replace('.', ''))
            elif infoClass.text == "Kubikaža":
                kubikaza = int(infoValue.text.split()[0])
            elif infoClass.text == "Snaga motora":
                snaga_motora = int(infoValue.text.split()[0].split("/")[0])

        additionalInfo = allCarInfo.find('div', class_='js-tab-classified-content classified-content').find('div', class_='infoBox').find('div', class_='uk-grid js-hidden uk-margin-top')
        additionalInfoRows = additionalInfo.findAll('div', class_='divider')
        for additionalInfoRow in additionalInfoRows:
            infoClass = additionalInfoRow.find('div', class_='uk-width-1-2')
            infoValue = additionalInfoRow.find('div', class_='uk-width-1-2 uk-text-bold')
            if infoClass.text == "Boja":
                boja = infoValue.text
            elif infoClass.text == "Menjač":
                menjac = infoValue.text
            elif infoClass.text == "Broj vrata":
                broj_vrata = int(infoValue.text.split()[0].split("/")[0])
        database.insertCar(marka,model,cena,stanje,grad,godiste,karoserija,vrsta_goriva,boja,kubikaza,snaga_motora, kilometraza, menjac, broj_vrata)
        fetched_cars += 1
        print("-------------------------"+str(fetched_cars)+"------------------------------")
    page += 1
    print("\n\nFETCHING PAGE NUMBER " + str(page) + "...............\n")
database.closeConnection()
