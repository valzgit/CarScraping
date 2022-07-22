from database import DatabaseInteractor

database = DatabaseInteractor()
database.initConnection()
database.printCarNumberPerColor()
database.closeConnection()