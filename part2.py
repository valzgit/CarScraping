from database import DatabaseInteractor

database = DatabaseInteractor()
database.initConnection()
database.printRangList()
database.closeConnection()