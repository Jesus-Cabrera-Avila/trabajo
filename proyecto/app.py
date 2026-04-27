from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

uri = "mongodb+srv://24308060610607_db_user:J260909c@dmc5.af41dor.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client["mi_app"]
usuarios = db["usuarios"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("iniciar_sesion.html")

@app.route("/registro")
def registro():
    return render_template("formulario.html")

@app.route("/recuperar")
def recuperar():
    return render_template("recuperar_contraseña.html")

@app.route("/tareas")
def tareas():
    return render_template("gestor_tareas.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    usuario = request.form["usuario"]
    password = request.form["password"]

    user_existente = usuarios.find_one({"usuario": usuario})

    if user_existente:
        return render_template("formulario.html", error="Este correo ya está registrado")

    usuarios.insert_one({
        "usuario": usuario,
        "password": password
    })

    return redirect("/login")

@app.route("/iniciar", methods=["POST"])
def iniciar():
    usuario = request.form["usuario"]
    password = request.form["password"]

    user = usuarios.find_one({"usuario": usuario})

    if user and user["password"] == password:
        return redirect("/tareas")
    else:
        return render_template("iniciar_sesion.html", error="Usuario o contraseña incorrectos")

if __name__ == "__main__":
    app.run(debug=True)