import heapq

from car import Car
from database import DatabaseInteractor
import numpy as np
import pandas as pd

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
train_cars, test_cars = Car.separateIntoTrainAndTestData(cars, 99)
guessed_bucket_classes = ["guessed [<= 2000]", "guessed [<= 4999]", "guessed [<= 9999]", "guessed [<= 14999]",
                          "guessed [<= 19999]", "guessed [<= 24999]", "guessed [<= 29999]", "guessed [> 30000]"]
bucket_classes = ["<= 2000", "<= 4999", "<= 9999", "<= 14999", "<= 19999", "<= 24999", "<= 29999", "> 30000"]
bucket_matrix = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
initial_k = round(np.sqrt(len(train_cars)))

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

    # print("Guessed [" + bucket_classes[max_position]+"]" + " and real was [" + bucket_classes[test_car.getPriceBucketIndex()] + "]")
    # print(pd.DataFrame(bucket_matrix, columns=bucket_classes, index = guessed_bucket_classes).to_string())
print(pd.DataFrame(bucket_matrix, columns=bucket_classes, index=guessed_bucket_classes).to_string())

memorized_accuracies = []
top_A = 0
bottom_A = 0
i = 0
j = 0
while i < len(bucket_matrix):
    while j < len(bucket_matrix[0]):
        if i == j:
            top_A += bucket_matrix[i][j]
        bottom_A += bucket_matrix[i][j]
        j += 1
    i += 1
A = top_A / bottom_A
print("Accuracy is [A = " + str(A) + "]")
memorized_accuracies.append([initial_k, A])

while 1:
    try:
        print("Unesite karoseriju")
        temp_karoseriju = input()
        print("Unesite gorivo")
        temp_gorivo = input()
        print("Unesite menjac")
        temp_menjac = input()
        print("Unesite marku")
        temp_marku = input()
        print("Unesite model")
        temp_model = input()
        print("Unesite stanje")
        temp_stanje = input()
        print("Unesite godiste")
        temp_godiste = int(input())
        print("Unesite kubikazu")
        temp_kubikaza = int(input())
        print("Unesite snagu motora")
        temp_snaga = int(input())
        print("Unesite kilometrazu")
        temp_kilometraza = int(input())
        auto_za_proveru = Car(0, temp_marku, temp_model, 0, temp_stanje, "Beograd", temp_godiste, temp_karoseriju,
                              temp_gorivo, "Crna", temp_kubikaza, temp_snaga, temp_kilometraza,
                              temp_menjac, 4)
        params = auto_za_proveru.getLinearParams()
        for car in cars:
            pass
    except:
        print("Try again!")
database.closeConnection()
