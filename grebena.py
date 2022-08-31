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
# bilo je 0.35 i 1
alpha = 0.35
lambda_param = 1
for param in cars[0].getLinearParams():
    w.append(INITIAL_W)

iterations = 50
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
        grebena = 0
        if koje_w_se_azurira != 0:
            grebena = w[koje_w_se_azurira] * lambda_param
        novo_w.append(w[koje_w_se_azurira] - (alpha / m) * (Calculator.mulOfSameArrays(razlike, matrix[koje_w_se_azurira]) + grebena))
        koje_w_se_azurira += 1
    w = novo_w
    i += 1

print("Equasion parameters = " + str(w))
# w = [-2010.9133632477037, 4119.290700493879, 364.6330174944238, 4139.173257619237, 1370.4913928531266, 5782.97566149342, 170.09077424705043, 1363.806733922234, 1.1276311096421323, 1121.0550150905563, -640.2214017080361]
for test_car in test_cars:
    params = test_car.getLinearParams()
    h = w[0]
    index = 1
    while index != len(w):
        h += w[index] * params[index - 1]
        index += 1
    print("Predikcija = " + str(h) + " prava cena = " + str(test_car.cena))
# while 1:
#     try:
#         print("Unesite karoseriju")
#         temp_karoseriju = input()
#         print("Unesite gorivo")
#         temp_gorivo = input()
#         print("Unesite menjac")
#         temp_menjac = input()
#         print("Unesite marku")
#         temp_marku = input()
#         print("Unesite model")
#         temp_model = input()
#         print("Unesite stanje")
#         temp_stanje = input()
#         print("Unesite godiste")
#         temp_godiste = int(input())
#         print("Unesite kubikazu")
#         temp_kubikaza = int(input())
#         print("Unesite snagu motora")
#         temp_snaga = int(input())
#         print("Unesite kilometrazu")
#         temp_kilometraza = int(input())
#         auto_za_proveru = Car(0, temp_marku, temp_model, 0, temp_stanje, "Beograd", temp_godiste, temp_karoseriju, temp_gorivo, "Crna", temp_kubikaza, temp_snaga, temp_kilometraza,
#             temp_menjac, 4)
#         params = auto_za_proveru.getLinearParams()
#         h = w[0]
#         index = 1
#         for param in params:
#             h += w[index] * param
#             index += 1
#         print("Predikcija = " + str(h))
#     except:
#         print("Try again!")
database.closeConnection()
