from flask import Flask
import random

app = Flask(__name__)

listF = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
        "Según un estudio realizado en 2018, más del 50 por ciento de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
        "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
        "Según un estudio de 2019, más del 60 por ciento de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
        "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo"]

listE = ["Cara",
         "Sello"]

@app.route("/a")
def index():
    return f'<a href="/random_fact">'"¡Ver un dato aleatorio!"'</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(listF)}</p>'

@app.route
def cara_o_sello():
    resultado = random.choice(["Cara", "Sello"])
    return f"<p>Resultado del lanzamiento: {resultado}</p>"

app.run(debug=True)
