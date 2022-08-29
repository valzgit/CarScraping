from sklearn.linear_model import LinearRegression

from car import Car
from database import DatabaseInteractor

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
x_train,y_train = Car.splitXandY(train_cars)
x_test,y_test = Car.splitXandY(test_cars)
regressor = LinearRegression()
regressor.fit(x_train,y_train)
r2_score = regressor.score(x_test,y_test)
print(r2_score*100,'%')