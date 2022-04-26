import sqlite3


class data:

    def __init__(self,name):
        self.data_name = name
        #self.cursor = self.conn.cursor()
 

    def connect(self):
        self.conn = sqlite3.connect(self.data_name)

    def deco(self):
        self.conn.close()

    def naissances(self):
        #jour/mois/année de naissance
        with self.conn as cursor:
            return cursor.execute("SELECT date FROM animaux, animaux_velages, velages WHERE animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id ORDER BY date").fetchall()

    def familles(self):
        fam = []
        with self.conn as cursor:
            for row in cursor.execute("SELECT id, nom FROM familles"):
                fam.append(row)
            return fam
            
        with self.conn as cursor:
            return cursor.execute("SELECT id, nom FROM familles").fetchall()

    def mort_premat(self):
        with self.conn as cursor:
            pass #a trouver

    def famille_en_vie(self):
        with self.conn as cursor:
            return cursor.execute("SELECT famille_id FROM animaux, animaux_velages, velages WHERE animaux.mort_ne = 0 AND animaux.decede = 0 AND animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id").fetchall()
    