![GitHub Contributors Image](https://contrib.rocks/image?repo=Your_GitHub_Username/Your_GitHub_Repository_Name)


# LINFO1002
Projet 2  : site avec des graphiques de vache

## A faire dans l'ordre:

# POUR MAC

Clone/dowload le repo

```
git clone https://github.com/thomasdevl/LINFO1002
```
si ca ne fonctionne pas télécharger directement le zip sur github


### Lancer un terminal depuis le dossier LINFO1002

```
cd LINFO1002
```

### Installation de flask

pre : avoir python => aller le télécharger sur le site officiel 

```
pip3 install flask
```

### Lancement du site

```
cd flasktuto
cd flaskr
export FLASK_APP=__init__.py
```

```
flask run 
OU
python3 __init__.py
```
Aller sur le site : http://127.0.0.1:5000 


# POUR WINDOWS

### Installation et run du projet

Clone/dowload le repo

pre : avoir installer git et python

```
git clone https://github.com/thomasdevl/LINFO1002
cd flasktuto
cd flaskr
```
si ca ne fonctionne pas télécharger directement le zip sur github

### Venv

```
py -3 -m venv venv
.\venv\Scripts\activate
```
(venv) devrait apparaître 

### Instalation de Flask

```
pip install flask
```

### Lancer le serv

```
python __init__.py
```

Aller sur le site : http://127.0.0.1:5000 

# En cas de soucis

Si le site ne se lance pas des sceenshots avec explication du site sont disponibles:
LINFO1002/flasktuto/screen/Screen_avec_explication.pdf

Si vous avez encore des questions : Thomas_devl#1198(discord)

# Arborecense des fichiers

```
LINFO1002
├──flasktuto
│  ├──flaskr //dossier principal du site
│  │   ├── __init__.py //fichier de lancement 
│  │   ├── moon.py //calcul les dates de pleine lune
│  │   ├── db  // dossier pour la database
│  │   │    ├── 1002-sql-data //fichiers pour remplir la database
│  │   │    ├── create_db.py //Programme python qui crée la database et rajoute les éléments dedans
│  │   │    ├── create_db.sql //template de la databse
│  │   │    ├── dat.py //class py qui permet de se connecter à la database et prendre des données
│  │   │    ├── database.sqlite //la database
│  │   │    └── heritage.py //Programme python qui calcul l'héritage génétique de chaque vache et le rajoute à la database
│  │   ├── static //tous les fichiers statiques
│  │   │    ├── style.css
│  │   │    └── + des photos de vaches
│  │   ├── templates
│  │   │    ├── about.html //partie about du site
│  │   │    ├── base.html //base du side sidebar et titre
│  │   │    └── index.html //la home page + Tout ce qui crée les graphs en Javascript
│  │   └── __pycache__
│  └── screen
│      ├── Screen_avec_explication.pdf
│      └── + screenshot du site // /!\ A lire si le site ne se lance pas 
├──LICENSE
└──README.md
```


