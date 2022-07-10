CREATE TABLE automobil (
id BIGSERIAL NOT NULL PRIMARY KEY,
marka VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
cena INT NOT NULL,
stanje VARCHAR(50) NOT NULL,
grad VARCHAR(50) NOT NULL,
godiste INT NOT NULL,
karoserija VARCHAR(50) NOT NULL,
vrsta_goriva VARCHAR(50) NOT NULL,
boja VARCHAR(50) NOT NULL,
kubikaza INT NOT NULL,
snaga_motora VARCHAR(30) NOT NULL,
kilometraza INT NOT NULL,
menjac VARCHAR(50) NOT NULL,
broj_vrata VARCHAR(50) NOT NULL);