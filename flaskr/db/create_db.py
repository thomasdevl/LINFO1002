import sqlite3
import os

def main():

    # Accès à la base de données dans database.db
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    #creer la base apd du fichier create_db.sql
    with open("create_db.sql") as file:
        content = file.read()
     



    #inserer les données dans la db apd de 1002_sql-data




if __name__ == '__main__':
    main()