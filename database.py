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

    def closeConnection(self):
        if self.connection is not None:
            self.connection.close()
