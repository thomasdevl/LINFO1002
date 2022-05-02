# LINFO1002
Projet 2  : site avec des graph de vache

## A faire dans l'ordre:

# POUR MAC

Clone/dowload le repo

```
git clone https://github.com/thomasdevl/LINFO1002
```
si ca ne fonctionne pas télécharger directement le zip sur github


### Lancer un terminal depuis le dossier flaskuto

click droit sur le dossier>services>New terminal at folder

```
cd flasktuto
```

### Installation de flask

```
pip3 install flask
```
Pour vérifier que flask est bien installer :

```
flask --version
```

### Lancement du site

```
export FLASK_APP=flasktuto
export FLASK_ENV=development
flask run
```
Aller sur le site : http://127.0.0.1:5000 


# POUR WINDOWS

### Installation et run du projet

Clone/dowload le repo

```
git clone https://github.com/thomasdevl/LINFO1002
cd flasktuto
```
le terminal doit se situer sur le dossier tutoflaskr

py -3 -m venv venv

### Instalation de Flask
```
pip install flask
```

### Lancer le serv
```
python flaskr/__init__.py
```

Aller sur le site : http://127.0.0.1:5000 

# Arborecense des fichiers

```
LINFO1002
├──flasktuto
│  └──flaskr
│      ├── __init__.py
│      ├── moon.py
│      ├── db
│      │    ├── 1002-sql-data
│      │    ├── create_db.py
│      │    ├── create_db.sql
│      │    ├── dat.py
│      │    ├── database.sqlite
│      │    └── heritage.py
│      ├── static
│      │    ├── style.css
│      │    └── + des photos de vaches
│      ├── templates
│      │    ├── about.html
│      │    ├── base.html
│      │    └── index.html
│      └── __pycache__
├──LICENSE
└──README.md

```


