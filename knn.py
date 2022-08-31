import heapq

from car import Car
from database import DatabaseInteractor
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

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
train_cars, test_cars = Car.separateIntoTrainAndTestData(cars, 99.94)
guessed_bucket_classes = ["guessed [<= 2000]", "guessed [<= 4999]", "guessed [<= 9999]", "guessed [<= 14999]",
                          "guessed [<= 19999]", "guessed [<= 24999]", "guessed [<= 29999]", "guessed [> 30000]"]
bucket_classes = ["<= 2000", "<= 4999", "<= 9999", "<= 14999", "<= 19999", "<= 24999", "<= 29999", "> 30000"]
initial_k = round(np.sqrt(len(train_cars)))
print("Unesite k ili 0 ako zelite da algoritam sam racuna")
uneto_k = int(input())
if uneto_k <=0:
    min_k = round(9 / 10 * initial_k)
    max_k = round(11 / 10 * initial_k)
else:
    min_k = uneto_k
    print("Unesite max_k")
    max_k = int(input())
print("Testing k values from " + str(min_k) + " to " + str(max_k))
memorized_accuracies = []
while min_k <= max_k:
    bucket_matrix = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]]
    for test_car in test_cars:
        minHeap = []
        train_car_iterator = 0
        while train_car_iterator < len(train_cars):
            train_car = train_cars[train_car_iterator]
            distance = Car.calculateEuclideanDistance(test_car, train_car)
            minHeap.append([distance, train_car_iterator, train_car])
            train_car_iterator += 1

        heapq.heapify(minHeap)
        buckets = [0, 0, 0, 0, 0, 0, 0, 0]
        while_counter = 0
        while while_counter < initial_k:
            distance, unimportant, car = minHeap[while_counter]
            Car.enrichPriceBucket(car, buckets)
            while_counter += 1

        maximum = 0
        max_position = -1
        counter = 0
        while counter < len(buckets):
            if buckets[counter] > maximum:
                maximum = buckets[counter]
                max_position = counter
            counter += 1

        bucket_matrix[max_position][test_car.getPriceBucketIndex()] += 1

        print("Guessed [" + bucket_classes[max_position] + "]" + " and real was [" + bucket_classes[
            test_car.getPriceBucketIndex()] + "]")
        # print(pd.DataFrame(bucket_matrix, columns=bucket_classes, index = guessed_bucket_classes).to_string())
    print(pd.DataFrame(bucket_matrix, columns=bucket_classes, index=guessed_bucket_classes).to_string())

    top_A = 0
    bottom_A = 0
    i = 0
    j = 0

    while i < 8:
        while j < 8:
            if i == j:
                top_A += bucket_matrix[i][j]
            bottom_A += bucket_matrix[i][j]
            j += 1
        j = 0
        i += 1
    print("Top A = " + str(top_A))
    print("Bottom A = " + str(bottom_A))
    A = top_A / bottom_A
    print("Accuracy when k is [" + str(min_k) + "] is [A = " + str(A) + "]")
    memorized_accuracies.append([str(min_k), [min_k, A]])
    min_k += 1

for p, (x, y) in memorized_accuracies:
    plt.scatter(x, y, label=("k=" + str(p)))
plt.legend()
plt.show()

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
#         auto_za_proveru = Car(0, temp_marku, temp_model, 0, temp_stanje, "Beograd", temp_godiste, temp_karoseriju,
#                               temp_gorivo, "Crna", temp_kubikaza, temp_snaga, temp_kilometraza,
#                               temp_menjac, 4)
#         params = auto_za_proveru.getLinearParams()
#         for car in cars:
#             pass
#     except:
#         print("Try again!")
database.closeConnection()
