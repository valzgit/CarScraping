import random


class Car:
    max_car_godiste = 0
    max_car_kubikaza = 0
    max_car_snaga_motora = 0
    models = []
    price_ordered_models = []
    price_ordered_markas = []
    price_ordered_menjaci = []
    price_ordered_gorivo = []
    price_ordered_karoserija = []

    def __init__(self, car_id, marka, model, cena, stanje, grad, godiste, karoserija, vrsta_goriva, boja, kubikaza,
                 snaga_motora, kilometraza, menjac, broj_vrata):
        self.car_id = car_id
        self.marka = marka
        self.model = model
        self.cena = cena
        self.stanje = stanje
        self.grad = grad
        self.godiste = godiste
        self.karoserija = karoserija
        self.vrsta_goriva = vrsta_goriva
        self.boja = boja
        self.kubikaza = kubikaza
        self.snaga_motora = snaga_motora
        self.kilometraza = kilometraza
        self.menjac = menjac
        self.broj_vrata = broj_vrata

    @staticmethod
    def calculateNormalizationValues(cars):
        for car in cars:
            if car.godiste > Car.max_car_godiste:
                Car.max_car_godiste = car.godiste
            if car.kubikaza > Car.max_car_kubikaza:
                Car.max_car_kubikaza = car.kubikaza
            if car.snaga_motora > Car.max_car_snaga_motora:
                Car.max_car_snaga_motora = car.snaga_motora

    def getLinearParams(self):
        return [Car.generateNumberFromKaroserija(self.karoserija)/8,Car.generateNumberFromGorivo(self.vrsta_goriva)/5,Car.generateNumberFromMenjac(self.menjac)/6,Car.generateNumberFromMarka(self.marka)/64, Car.generateNumberFromModel(self.model)/782, Car.turnStanjeToNumber(self.stanje)/2,
                (self.godiste-1940)/82 ,
                self.kubikaza/ 2000103 , self.snaga_motora/581, self.kilometraza/3800006]

    @staticmethod
    def generateArrayFromMarka(car_marka):
        array = []
        markas = [
            "Mahindra",
            "Ford",
            "Smart",
            "Maserati",
            "Dodge",
            "Infiniti",
            "MINI",
            "Bentley",
            "Peugeot",
            "Rolls Royce",
            "Dacia",
            "Piaggio",
            "Moskvitch",
            "Audi",
            "MG",
            "Lexus",
            "Great Wall",
            "NSU",
            "Jeep",
            "Volvo",
            "Cadillac",
            "Lancia",
            "Suzuki",
            "Mitsubishi",
            "Mercedes Benz",
            "Ferrari",
            "Chrysler",
            "Wartburg",
            "Isuzu",
            "UAZ",
            "Lincoln",
            "Honda",
            "Shuanghuan",
            "Daewoo",
            "Chevrolet",
            "Daihatsu",
            "Aro",
            "Tata",
            "Škoda",
            "Zastava",
            "Porsche",
            "Alfa Romeo",
            "Lada",
            "Rover",
            "Jaguar",
            "Renault",
            "Kia",
            "Chery",
            "Fiat",
            "Land Rover",
            "Trabant",
            "Opel",
            "Nissan",
            "Saab",
            "Hyundai",
            "Citroen",
            "Subaru",
            "Mazda",
            "BMW",
            "Volkswagen",
            "Seat",
            "SsangYong",
            "Hummer",
            "Toyota"
        ]
        for model in markas:
            if car_marka == model:
                array.append(1)
            else:
                array.append(0)
        return array

    @staticmethod
    def generateNumberFromModel(car_model):
        index = 0
        while index < len(Car.price_ordered_models):
            if Car.price_ordered_models[index] == car_model:
                return index + 1
            index += 1
        return 0

    @staticmethod
    def generateNumberFromKaroserija(car_karoserija):
        index = 0
        while index < len(Car.price_ordered_karoserija):
            if Car.price_ordered_karoserija[index] == car_karoserija:
                return index + 1
            index += 1
        return 0

    @staticmethod
    def generateNumberFromGorivo(car_gorivo):
        index = 0
        while index < len(Car.price_ordered_gorivo):
            if Car.price_ordered_gorivo[index] == car_gorivo:
                return index + 1
            index += 1
        return 0

    @staticmethod
    def generateNumberFromMarka(car_marka):
        index = 0
        while index < len(Car.price_ordered_markas):
            if Car.price_ordered_markas[index] == car_marka:
                return index + 1
            index += 1
        return 0

    @staticmethod
    def generateNumberFromMenjac(car_menjac):
        index = 0
        while index < len(Car.price_ordered_menjaci):
            if Car.price_ordered_menjaci[index] == car_menjac:
                return index + 1
            index += 1
        return 0

    @staticmethod
    def generateArrayFromModel(car_model):
        array = []
        for model in Car.models:
            if car_model == model:
                array.append(1)
            else:
                array.append(0)
        return array

    @staticmethod
    def turnStanjeToNumber(car_stanje):
        polovnoca = [
            "Novo vozilo",
            "Polovno vozilo"
        ]
        if car_stanje == polovnoca[0]:
            return 2
        else:
            return 1

    @staticmethod
    def separateIntoTrainAndTestData(cars, percentage):
        split_index = round(percentage / 100.0 * len(cars))
        return cars[:split_index], cars[split_index:]

    @staticmethod
    def removeAllCarsThatHaveOutOfRangeNumericalParams(cars):
        cars.sort(key=lambda x: x.kubikaza, reverse=True)
        size = len(cars)
        cars = cars[50:size - 50]

        cars.sort(key=lambda x: x.godiste, reverse=True)
        size = len(cars)
        cars = cars[50:size - 50]

        cars.sort(key=lambda x: x.snaga_motora, reverse=True)
        size = len(cars)
        cars = cars[50:size - 50]

        cars.sort(key=lambda x: x.kilometraza, reverse=True)
        size = len(cars)
        cars = cars[50:size - 50]

        cars.sort(key=lambda x: x.cena, reverse=False)

        minimum_index = 0
        while cars[minimum_index].cena < 450:
            minimum_index += 1

        maxiumum_index = len(cars) - 1
        while cars[maxiumum_index].cena > 45000:
            maxiumum_index -= 1

        cars = cars[minimum_index:maxiumum_index]

        return cars

    # @staticmethod
    # def removeCarsThatHaveInvalidParams(cars):
    #     counter = 0
    #     indexes = []
    #     while counter < len(cars):
    #         if cars[counter].kubikaza > 6500:
    #             indexes.append(counter)
    #         counter += 1
    #     for index in reversed(indexes):
    #         cars.pop(index)
    @staticmethod
    def shuffle(cars):
        random.shuffle(cars)

    @staticmethod
    def splitXandY(cars):
        x_train = []
        y_train = []
        for car in cars:
            x_train.append(Car.getLinearParams(car))
            y_train.append(car.cena)
        return x_train, y_train
