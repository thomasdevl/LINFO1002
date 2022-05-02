#fonction pour calculer l'héritage génétique 
import sqlite3


def recup_races(conn,a):
    #recup la race de l'animal grace a son id
    with conn as cursor:
        return cursor.execute("SELECT type_id, pourcentage FROM animaux_types WHERE animal_id = ?", (a,)).fetchall()

def recup_parents(conn,a):
    #recup la race des parents 
    with conn as cursor:
        return cursor.execute("SELECT pere_id, mere_id FROM animaux, animaux_velages, velages WHERE animaux.id = ? AND animaux.id = animaux_velages.animal_id AND animaux_velages.animal_id = velages.id",(a,)).fetchall()


def calcul_race(race_parent):

    dic = {}
    for race in race_parent:
        dic[race[0]] = dic.get(race[0], 0)+ race[1]

    a = []
    #retour a un tuple 
    for race in dic.items():
        a.append((race[0], race[1] / 2))

    return a


def race_vers_db(conn,id,race):

    #rajouter la race qui a été calculé dans la database
    for r in race:
        with conn as cursor:
            cursor.execute("INSERT INTO animaux_types VALUES (?, ?, ?)", (id, r[0], r[1]))
            print(f"added : id :{id} , type: {r[0]} ,pourct : {r[1]}")
    


def set_races(conn,id):
    
    #récup les parents de la vache
    if type(id) == tuple:
        idc = id[0]
    else:
        idc = id
    
    parents = recup_parents(conn, idc)

    if len(parents) == 0 : #si pas de parents :(
        return recup_races(conn,idc)

    pere = parents[0][0]
    mere = parents[0][1]

    #récup races des parents
    race_mere = recup_races(conn, int(mere))
    race_pere = recup_races(conn, int(pere))

    #si les parents n'ont pas de race calculé la leur en premier
    if len(race_mere) == 0:
        race_mere = set_races(conn, mere)

    if len(race_pere) == 0:
        race_pere = set_races(conn, pere)

    race = calcul_race(race_mere +race_pere)

    race_vers_db(conn,idc,race)

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
        races.append(recup_races(conn,id[0]))

        if races[0] == []:
            set_races(conn,id)
    