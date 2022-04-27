import os
import pathlib
import sqlite3

from flask import Flask, redirect , url_for, render_template

from flaskr.db.dat import data

app = Flask(__name__)

fromage = data(os.path.join(pathlib.Path(__file__).parent.absolute(), "db/database.sqlite"))

@app.route("/")
def home():

	#chopper tt les bails dans la base de donnée
	fromage.connect()

	#famille 
	fam = fromage.familles()


	fam_id = []
	for f in fam:
		fam_id.append(f[0])

	fam_names = []
	for f in fam:
		fam_names.append(f[1].strip())


	#famille en vie 
	fam_en_v = fromage.famille_en_vie()

	#naissance 
	naiss = fromage.naissances() #lst de toutes les dates de naissances 

	#dico avec le nmbr de naissance par jour 
	d_naiss = dict()
	for i in naiss:
		d_naiss[i] = d_naiss.get(i, 0) + 1

	fromage.deco()

	graph_data = {
		"famille" :fam,
		"famille_id": fam_id,
		"famille_names" : fam_names,
		"famille_en_vie" : fam_en_v,
		"naissance" : naiss,
		"naissance_dico" : d_naiss
	}

	return render_template("index.html",graph_data=graph_data) 


@app.route("/about")
def about():
	return render_template("about.html")



if __name__ == "__main__":
	app.run(debug=True)