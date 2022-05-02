import sqlite3


class data:
    '''
    Class qui va premettre de se connecter a la database et récupérér les valeurs
    Pre: le nom d'une database 
    '''

    def __init__(self,name):
        self.data_name = name
 
    def connect(self):
        '''
        connection a la database.
        Pre: le nom d'une database valide
        '''
        self.conn = sqlite3.connect(self.data_name)

    def deco(self):
        '''
        déconnection de la data base
        '''
        self.conn.close()

    def naissances(self):
        '''
        Post: une liste avec toutes les naissances en format dd/mm/yyyy
        '''
        with self.conn as cursor:
            return cursor.execute("SELECT date FROM animaux, animaux_velages, velages WHERE animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id ORDER BY date").fetchall()

    def race_naissance(self,lst_date):
        '''
        Pre: une list de jour en format dd/mm/yyyy
        Post: une liste avec le type de vache et son pourcentage qui son nait ce jour la 
        en format : [date $ (type,pourcentage)!]
        '''
        lst = []
        for date in lst_date:
            with self.conn as cursor:
                a = cursor.execute("SELECT animaux_types.type_id,animaux_types.pourcentage FROM animaux_types,velages,animaux_velages WHERE velages.date = ? AND velages.id = animaux_velages.velage_id AND animaux_velages.animal_id = animaux_types.animal_id",(date)).fetchall()
                lst.append(f"{date}${a}!")
        return lst

    def familles(self):
        '''
        Post: une liste avec toutes les familles
        '''
        #[date $ (type,pourcentage)!]
        #liste avec toutes les familles 
        fam = []
        with self.conn as cursor:
            for row in cursor.execute("SELECT id, nom FROM familles"):
                fam.append(row)
            return fam

    def famille_en_vie(self):
        '''
        Post: une liste avec l'id de toutes les familles en vie 
        '''
        with self.conn as cursor:
            return cursor.execute("SELECT famille_id FROM animaux, animaux_velages, velages WHERE animaux.mort_ne = 0 AND animaux.decede = 0 AND animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id").fetchall()

    def lst_type_pourct(self):
        '''
        Post: une liste avec le type et le pourcentage de race
        '''
        with self.conn as cursor:
            return cursor.execute("SELECT type_id, pourcentage FROM animaux_types").fetchall()

        
    