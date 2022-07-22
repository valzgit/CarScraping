import psycopg2


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

    def closeConnection(self):
        if self.connection is not None:
            self.connection.close()
