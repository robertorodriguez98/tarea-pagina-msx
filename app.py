from flask import Flask, render_template, request,abort
from funciones import LeerLibreria
import os

libreria = LeerLibreria()

app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos')
def juegos():
    listaCat = []
    for juego in libreria:
        if juego.get("categoria") not in listaCat:
            listaCat.append(juego.get("categoria"))
    return render_template("juegos.html", listaCat = listaCat)

@app.route('/juegos',methods=["POST"])
def listajuegos():
    nuevalibreria = []
    juegobusc=request.form['juego']
    catbusc=request.form['categoria']
    for juego in libreria:
        nombre = str(juego.get("nombre"))
        if nombre.startswith(str(juegobusc)) and juego.get("categoria") == catbusc:
            dict={"nombre":juego.get("nombre"),"desarrollador":juego.get("desarrollador"),"id":juego.get("id")}
            nuevalibreria.append(dict) 
    listaCat = []
    for juego in libreria:
        if juego.get("categoria") not in listaCat:
            listaCat.append(juego.get("categoria"))           
    return render_template("listajuegos.html", libreria=nuevalibreria,juegobusc=juegobusc,listaCat=listaCat,catbusc=catbusc)

@app.route('/juego/<id>')
def juego(id):
    for juego in libreria:
        if juego.get("id") == int(id):
            return render_template("juego.html",juego=juego)
    abort(404)

#app.run("0.0.0.0",5000,debug=True)
port=os.environ["PORT"]
app.run("0.0.0.0",int(port),debug=True)