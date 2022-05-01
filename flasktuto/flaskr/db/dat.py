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
        #liste avec toutes les naissance en jour/mois/année de naissance
        with self.conn as cursor:
            return cursor.execute("SELECT date FROM animaux, animaux_velages, velages WHERE animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id ORDER BY date").fetchall()


    def race_naissance(self,lst_date):
        #lst avec la date et les races 
        #[date $ (type,pourcentage)!]

        lst = []

        for date in lst_date:

            with self.conn as cursor:
                a = cursor.execute("SELECT animaux_types.type_id,animaux_types.pourcentage FROM animaux_types,velages,animaux_velages WHERE velages.date = ? AND velages.id = animaux_velages.velage_id AND animaux_velages.animal_id = animaux_types.animal_id",(date)).fetchall()
                lst.append(f"{date}${a}!")

        return lst


    def familles(self):
        #liste avec toutes les familles 
        fam = []
        with self.conn as cursor:
            for row in cursor.execute("SELECT id, nom FROM familles"):
                fam.append(row)
            return fam


    def mort_premat_fam(self):
        fam = []
        with self.conn as cursor:
            for row in cursor.execute("SELECT id, nom FROM familles"):
                fam.append(row)
            return fam
            

    def famille_en_vie(self):
        with self.conn as cursor:
            return cursor.execute("SELECT famille_id FROM animaux, animaux_velages, velages WHERE animaux.mort_ne = 0 AND animaux.decede = 0 AND animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id").fetchall()

    def lst_type_pourct(self):
        with self.conn as cursor:
            return cursor.execute("SELECT type_id, pourcentage FROM animaux_types").fetchall()

        
    