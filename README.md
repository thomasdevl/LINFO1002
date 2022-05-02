# LINFO1002
Projet 2  : site avec des graph de vache

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
export FLASK_APP=flasktuto
export FLASK_ENV=development
cd flaskr
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

# Arborecense des fichiers

```
LINFO1002
├──flasktuto
│  ├──flaskr
│  │   ├── __init__.py
│  │   ├── moon.py
│  │   ├── db
│  │   │    ├── 1002-sql-data
│  │   │    ├── create_db.py
│  │   │    ├── create_db.sql
│  │   │    ├── dat.py
│  │   │    ├── database.sqlite
│  │   │    └── heritage.py
│  │   ├── static
│  │   │    ├── style.css
│  │   │    └── + des photos de vaches
│  │   ├── templates
│  │   │    ├── about.html
│  │   │    ├── base.html
│  │   │    └── index.html
│  │   └── __pycache__
│  └── screen
│      ├── Screen_avec_explication.pdf
│      └── + screenshot du site
├──LICENSE
└──README.md
```


