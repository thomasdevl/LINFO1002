import os
import pathlib
import sqlite3

from flask import Flask, redirect , url_for, render_template

from db.dat import data
from moon import dico_naiss_lune

app = Flask(__name__)

fromage = data(os.path.join(pathlib.Path(__file__).parent.absolute(), "db/database.sqlite"))

#prendre tt les données dans la base de donnée
fromage.connect()

#famille 
fam = fromage.familles()

#lst avec les id des vaches
fam_id = []
for f in fam:
	fam_id.append(f[0])
#lst avec les noms des vaches
fam_names = []
for f in fam:
	fam_names.append(f[1].strip())

#famille en vie 
fam_en_v = fromage.famille_en_vie()

#naissance 
naiss = fromage.naissances() #lst de toutes les dates de naissances 

#liste avec [date : type pourcentage]
lst_datetype = fromage.race_naissance(naiss)

#dico avec le nmbr de naissance par jour 
d_naiss = dict()
for i in naiss:
	d_naiss[i] = d_naiss.get(i, 0) + 1

#dico date + lune 
d_lune = dico_naiss_lune(naiss)

#lst avec race et pourcentage
lst_type_pourct = fromage.lst_type_pourct()

#lst avec famille et date de naissance
lst_datefam = fromage.fam_naissance(naiss)

familles = fromage.familles()

fromage.deco()

graph_data = {
	"famille" :fam,
	"famille_id": fam_id,
	"famille_names" : fam_names,
	"famille_en_vie" : fam_en_v,
	"naissance" : naiss,
	"naissance_dico" : d_naiss,
	"lst_datetype" : lst_datetype,
	"dico_lune" : d_lune,
	"lst_type_pourct" :lst_type_pourct,
	"lst_datefam" : lst_datefam,
	'familles': familles
}

@app.route("/")
def home():
	return render_template("index.html",graph_data=graph_data) 


@app.route("/about")
def about():
	return render_template("about.html")


if __name__ == "__main__":
	app.run(debug=True)