import sqlite3
import heritage


def main():

    # Accès à la base de données dans database.db
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    
    #creer la base apd du fichier create_db.sql
    with open("create_db.sql",'r') as file:
        content = file.read()
    cursor.executescript(content)
    conn.commit()
    
    #inserer les données dans la db apd de 1002_sql-data
    files = ['insert_animaux_types.sql','insert_animaux_velages.sql', 'insert_animaux.sql', 'insert_complications.sql', 'insert_familles.sql', 'insert_types.sql', 'insert_velages_complications.sql', 'insert_velages.sql']

    for f in files:
        with open(f"1002-sql-data/{f}",'r') as file:
            insert_content = file.read()
            print(f"{f} : succes")
        cursor.executescript(insert_content)
        conn.commit()
                                
            
    #calcule héritage génétique et le rajoute dans la db
    heritage.heritage_gene(conn) 
    print(f"Héritage ajouté")

    conn.close()


if __name__ == '__main__':
    main()