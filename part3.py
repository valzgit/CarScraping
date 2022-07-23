from matplotlib import pyplot as plt
from database import DatabaseInteractor

database = DatabaseInteractor()
database.initConnection()

matrix = database.getCarNumberPerCity(10)
labels = []
sizes = []
explode = []
for row in matrix:
    labels.append(row[0])
    sizes.append(row[1])
    explode.append(0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


database.closeConnection()