import psycopg2

from car import Car


class DatabaseInteractor:
    hostname = 'localhost'
    database = 'cars'
    username = 'postgres'
    pwd = 'Password123'
    port_id = 5432
    cursor = None
    connection = None

    def initConnection(self):
        try:
            self.connection = psycopg2.connect(
                host=self.hostname,
                dbname=self.database,
                user=self.username,
                password=self.pwd,
                port=self.port_id)
        except Exception as error:
            print(error)

    def insertCar(self, marka, model, cena, stanje, grad, godiste, karoserija, vrsta_goriva, boja, kubikaza,
                  snaga_motora, kilometraza, menjac, broj_vrata):
        try:
            cursor = self.connection.cursor()

            insert_script = 'INSERT INTO automobil ' \
                            '(marka,model,cena,stanje,grad,godiste,karoserija,vrsta_goriva,boja,kubikaza,snaga_motora,kilometraza,menjac,broj_vrata)' \
                            'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            insert_value = (
                marka, model, cena, stanje, grad, godiste, karoserija, vrsta_goriva, boja, kubikaza, snaga_motora,
                kilometraza, menjac, broj_vrata)
            cursor.execute(insert_script, insert_value)
            self.connection.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()


    def printCarNumberPerType(self):
        try:
            cursor = self.connection.cursor()

            select_script = "select marka, count(*) as broj from automobil group by marka order by broj desc"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                for row in rows:
                 print("["+str(row[0]) + " | " + str(row[1])+"]")

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def getAllCars(self):
        try:
            cursor = self.connection.cursor()

            select_script = "select id, marka, model, cena, stanje, grad, godiste, karoserija, vrsta_goriva, boja, kubikaza, snaga_motora, kilometraza, menjac, broj_vrata from automobil"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                cars = []
                for row in rows:
                    cars.append(Car(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
            return cars

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def printCarNumberPerCity(self):
        try:
            cursor = self.connection.cursor()

            select_script = "select grad, count(*) as broj from automobil group by grad order by broj desc"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                for row in rows:
                 print("["+str(row[0]) + " | " + str(row[1])+"]")

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def printCarNumberPerColor(self):
        try:
            cursor = self.connection.cursor()

            select_script = "select boja, count(*) as broj from automobil group by boja order by broj desc"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print("[" + str(row[0]) + " | " + str(row[1]) + "]")

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def printMostExpensiveCars(self, broj, karoserija):
        try:
            cursor = self.connection.cursor()

            if karoserija is None:
                select_script = "select marka,model,karoserija,cena from automobil order by cena desc limit %s"
                select_values = (broj,)
                cursor.execute(select_script, select_values)
            else:
                select_script = "select marka,model,karoserija,cena from automobil where karoserija = %s order by cena desc limit %s"
                cursor.execute(select_script, (str(karoserija), str(broj)))



            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print("[" + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " | " + str(row[3]) + "e]")

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def printRangList(self):
        try:
            cursor = self.connection.cursor()

            select_script = "select marka,model,karoserija,cena from automobil where godiste = 2021 or godiste = 2022 order by cena desc"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print("[" + str(row[0]) + " | " + str(row[1]) +  " | " + str(row[2]) + " | " + str(row[3]) + "e]")

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def najvecaKubikaza(self):
        try:
            cursor = self.connection.cursor()

            select_script = "select marka,model,cena from automobil order by kubikaza desc limit 1"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print("[" + str(row[0]) + " | " + str(row[1]) +  " | " + str(row[2]) + "e]")

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def najvecaSnaga(self):
        try:
            cursor = self.connection.cursor()

            select_script = "select marka,model,cena from automobil order by snaga_motora desc limit 1"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print("[" + str(row[0]) + " | " + str(row[1]) +  " | " + str(row[2]) + "e]")

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def najvecaKilometraza(self):
        try:
            cursor = self.connection.cursor()

            select_script = "select marka,model,cena from automobil order by kilometraza desc limit 1"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print("[" + str(row[0]) + " | " + str(row[1]) +  " | " + str(row[2]) + "e]")

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def getCarNumberPerCity(self, limit):
        try:
            cursor = self.connection.cursor()

            select_params = (limit,)
            select_script = "select grad, count(*) as broj from automobil group by grad order by broj desc limit %s"

            cursor.execute(select_script, select_params)

            if cursor.rowcount == 0:
                return None
            else:
                rows = cursor.fetchall()
                matrix = []
                for row in rows:
                    matrix.append([str(row[0]), row[1]])

            return matrix
        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def closeConnection(self):
        if self.connection is not None:
            self.connection.close()

    def dohvatiSveKilometrazeIGodineICene(self):
        try:
            cursor = self.connection.cursor()
            select_script = "select kilometraza, godiste, cena from automobil"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                return cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()

    def brojSaAutomatskimIManuelnimMenjacem(self):
        try:
            cursor = self.connection.cursor()
            select_script = "select menjac, count(*) as broj from automobil group by menjac"

            cursor.execute(select_script)

            if cursor.rowcount == 0:
                return None
            else:
                return cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
                self.initConnection()