from calculator import Calculator
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
alpha = 0.35
for param in cars[0].getLinearParams():
    w.append(INITIAL_W)

iterations = 300
i = 0
while i < iterations:
    print("Iteration: " + str(i))
    print(w)

    matrix = []
    for param_w in w:
        matrix.append([])
    razlike = []
    for car in cars:
        params = car.getLinearParams()
        w_index = 1
        h_x = w[0]
        for param in params:
            matrix[w_index].append(param)
            h_x += w[w_index] * param
            w_index += 1

        razlike.append(h_x - car.cena)


    m = len(train_cars)
    novo_w = []
    koje_w_se_azurira = 0
    while koje_w_se_azurira < len(w):
        novo_w.append(w[koje_w_se_azurira] - (alpha/m) * Calculator.mulOfSameArrays(razlike, matrix[koje_w_se_azurira]))
        koje_w_se_azurira += 1
    w = novo_w
    i += 1

print("Equasion parameters = " + str(w))

for test_car in test_cars:
    params = test_car.getLinearParams()
    h = w[0]
    index = 1
    while index != len(w):
        h += w[index] * params[index-1]
        index += 1
    print("Predikcija = " + str(h) + " prava cena = " + str(test_car.cena))

database.closeConnection()
