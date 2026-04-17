from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)