from sklearn.linear_model import LinearRegression

from car import Car
from database import DatabaseInteractor

INITIAL_W = 1
database = DatabaseInteractor()
database.initConnection()
Car.models = database.getAllModels()
Car.price_ordered_models = database.getPriceOrderedModels()
Car.price_ordered_markas = database.getPriceOrderedMarkas()
Car.price_ordered_menjaci = database.getPriceOrderedMenjaci()
Car.price_ordered_gorivo = database.getPriceOrderedVrsteGoriva()
Car.price_ordered_karoserija = database.getPriceOrderedKaroserija()
cars = database.getAllCars()
print(len(cars))
cars = Car.removeAllCarsThatHaveOutOfRangeNumericalParams(cars)
print(len(cars))
Car.shuffle(cars)
Car.calculateNormalizationValues(cars)
train_cars, test_cars = Car.separateIntoTrainAndTestData(cars, 70)
w = [INITIAL_W]
alpha = 0.001
for param in cars[0].getLinearParams():
    w.append(INITIAL_W)

count = 0
for train_car in train_cars:
    count += 1
    params = train_car.getLinearParams()
    h = 0
    index = 0
    while index != len(params):
        h += w[index] * params[index]
        index += 1
    h += w[len(w) - 1]
    index = 0
    while index != len(w):
        if index != len(w) - 1:
            w[index] = w[index] - (1.0 * alpha / len(train_cars)) * (h - train_car.cena) * params[index]
        else:
            w[index] = w[index] - (1.0 * alpha / len(train_cars)) * (h - train_car.cena)
        index += 1

print("Equasion parameters = " + str(w))
for test_car in test_cars:
    params = test_car.getLinearParams()
    h = 0
    index = 0
    while index != len(params):
        h += w[index] * params[index]
        index += 1
    h += w[len(w) - 1]
    print("Predikcija = " + str(h) + " prava cena = " + str(test_car.cena))

database.closeConnection()
