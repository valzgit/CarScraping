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
# sveKilometraze = database.dohvatiSveKilometrazeIGodine()
# buckets = [0, 0, 0, 0, 0, 0, 0]
# for row in sveKilometraze:
#     buckets[min(int(int(row[0])/50000), len(buckets) - 1)] += 1
#
# data = {'ispod 50 000': buckets[0], '50 000 do 99 999' : buckets[1], '100 000 do 149 999': buckets[2], '150 000 do 199 999': buckets[3], '200 000 do 249 999': buckets[4], ' 250 000 do 299 999': buckets[5], 'preko 300 000': buckets[6]}
# names = list(data.keys())
# values = list(data.values())
# print(names)
# print(values)
#
# plt.bar(names,values)
# plt.show()

# zadatak 3
# sveGodine = database.dohvatiSveKilometrazeIGodine()
# buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for row in sveGodine:
#     if row[1] <= 2000:
#         index = max(int((int(row[1]) - 1950) / 10),
#                     0)  # starije od 1960 -> 1959-1950=9, pa /10 = 0, ako je manji broj negativan je tako da ce ga zaokruziti na 0
#         # 1960 do 1969 - 1950 = 10 do 19 /10 = 1 do 1 itd.
#         buckets[index] += 1
#     else:
#         if row[1] <= 2005:
#             buckets[5] += 1
#         elif row[1] <= 2010:
#             buckets[6] += 1
#         elif row[1] <= 2015:
#             buckets[7] += 1
#         elif row[1] <= 2020:
#             buckets[8] += 1
#         else:
#             buckets[9] += 1
#
# data = {'starije od 1960': buckets[0], '1961-1970': buckets[1], '1971-1980': buckets[2], '1981-1990': buckets[3],
#         '1991-2000': buckets[4], '2001-2005': buckets[5], '2006-2010': buckets[6], '2011-2015': buckets[7],
#         '2016-2020': buckets[8], '2021-2022': buckets[9]}
# names = list(data.keys())
# values = list(data.values())
# print(names)
# print(values)
#
# plt.bar(names, values)
# plt.show()

#zadatk 4
# matrix = database.brojSaAutomatskimIManuelnimMenjacem()
# labels = ['Automatski', 'Manuelni']
# explode = [0, 0]
#
# automatski = 0
# manuelni = 0
# for row in matrix:
#     if str(row[0]).__contains__('automatski'):
#         automatski+=row[1]
#     else:
#         manuelni+=row[1]
# sizes = [automatski, manuelni]
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()

# zadatak 5
sveGodine = database.dohvatiSveKilometrazeIGodineICene()
buckets = [0, 0, 0, 0, 0, 0, 0, 0]
for row in sveGodine:
    if row[2] <= 2000:
        buckets[0] += 1
    elif row[2] <= 4999:
        buckets[1] += 1
    elif row[2] <= 9999:
        buckets[2] += 1
    elif row[2] <= 14999:
        buckets[3] += 1
    elif row[2] <= 19999:
        buckets[4] += 1
    elif row[2] <= 24999:
        buckets[5] += 1
    elif row[2] <= 29999:
        buckets[6] += 1
    else:
        buckets[7] += 1

data = {'manje od 2000 €': buckets[0], '2000 € i 4999 €': buckets[1], '5000 € i 9999 €': buckets[2], '10 000 € i 14 999 €': buckets[3],
        '15 000 € i 19 999 €': buckets[4], '20 000 € i 24 999 €': buckets[5], '25 000 € i 29 999 €': buckets[6], '30 000 € ili više': buckets[7]}
names = list(data.keys())
values = list(data.values())
print(names)
print(values)

plt.bar(names, values)
plt.show()

database.closeConnection()