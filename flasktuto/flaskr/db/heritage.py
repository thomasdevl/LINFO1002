#fonction pour calculer l'héritage génétique 
import sqlite3


def recup_races(conn,id):
    #recup la race de l'animal grace a son id

    with conn as cursor:
        return cursor.execute("SELECT type_id, pourcentage FROM animaux_types WHERE animal_id = ?",(id)).fetchall()

def recup_parents(conn,id):
    #recup la race des parents 

    with conn as cursor:
        return cursor.execute("SELECT pere_id, mere_id FROM animaux, animaux_velages, velages WHERE animaux.id = ? AND animaux.id = animaux_velages.animal_id AND animaux_velages.animal_id = velages.id",(id,))


def calcul_race(race_mere,race_pere):

    #calcul la race de l'enfant apd de celle des parents
    race_parent = race_mere + race_pere

    dic = {}
    for race in race_parent:
        dic[race[0]] = dic.get(race[0], 0)+ race[1]

    a = []
    #retour a un tuple 
    for race in dic.items():
        a.append((race[0], race[1] / 2))

    return a


def race_vers_db(conn,id,race):
    for r in race:
        with conn as cursor:
            cursor.execute("INSERT INTO animaux_types VALUES (?, ?, ?)", (id, race[0], race[1]))
    


def set_races(conn,id):
    

    #récup les parents de la vache
    parents = recup_parents(conn, id)
    mere = parents[0]
    pere = parents[1]

    #récup races des parents
    race_mere = recup_races(conn, mere)
    race_pere = recup_races(conn, pere)

    #si les parents n'ont pas de race calculé la leur en premier
    if len(race_mere) == 0:
        race_mere = set_races(conn, mere)

    if len(race_pere) == 0:
        race_pere = set_races(conn, pere)

    race = calcul_race(race_mere,race_pere)

    race_vers_db(conn,id,race)

    return race

def heritage_gene(conn):
    
    #récup l'id de tous les animaux 
    lst_id = []
    with conn as cursor:
        for row in cursor.execute("SELECT id FROM animaux"):
            lst_id.append(row) 


    #pour chaque vache dans la db
    for id in lst_id:

        #recup la race de l'animal grace a son id
        races = []
        races.append(recup_races(conn,id))
        
        
        if len(races) == 0:
            set_races(conn,id)
    