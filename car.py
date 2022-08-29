class Car:
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

    def getLinearParams(self):
        return [int(self.godiste), int(self.kubikaza), int(self.snaga_motora), int(self.broj_vrata)]

    @staticmethod
    def separateIntoTrainAndTestData(cars, percentage):
        split_index = round(percentage / 100.0 * len(cars))
        return cars[:split_index], cars[split_index:]

    @staticmethod
    def removeAllCarsThatHaveInvalidParams(cars):
        cars.sort(key = lambda x: x.kubikaza, reverse = True)
        size = len(cars)
        cars = cars[50:size-50]

        cars.sort(key = lambda x: x.godiste, reverse = True)
        size = len(cars)
        cars = cars[50:size-50]

        cars.sort(key = lambda x: x.snaga_motora, reverse = True)
        size = len(cars)
        cars = cars[50:size-50]

        cars.sort(key = lambda x: x.broj_vrata, reverse = True)
        size = len(cars)
        return cars[50:size-50]

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
