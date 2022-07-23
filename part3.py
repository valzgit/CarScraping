from matplotlib import pyplot as plt
from database import DatabaseInteractor

database = DatabaseInteractor()
database.initConnection()

# zadatak 1

# matrix = database.getCarNumberPerCity(10)
# labels = []
# sizes = []
# explode = []
# for row in matrix:
#     labels.append(row[0])
#     sizes.append(row[1])
#     explode.append(0)
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()

# zadatak 2
sveKilometraze = database.dohvatiSveKilometraze()
buckets = [0, 0, 0, 0, 0, 0, 0]
for row in sveKilometraze:
    buckets[min(int(int(row[0])/50000), len(buckets) - 1)] += 1

data = {'ispod 50 000': buckets[0], '50 000 do 99 999' : buckets[1], '100 000 do 149 999': buckets[2], '150 000 do 199 999': buckets[3], '200 000 do 249 999': buckets[4], ' 250 000 do 299 999': buckets[5], 'preko 300 000': buckets[6]}
names = list(data.keys())
values = list(data.values())
print(names)
print(values)

plt.bar(names,values)
plt.show()

database.closeConnection()