from database import DatabaseInteractor

database = DatabaseInteractor()
database.initConnection()
database.najvecaKilometraza()
database.closeConnection()