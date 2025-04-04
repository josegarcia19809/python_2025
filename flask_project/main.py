from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Aprendiendo Flask"

@app.route("/informacion")
def informacion():
    return "<h1>Página de información</h1>"

@app.route("/contacto") # http://127.0.0.1:5000/contacto
def contacto():
    return "<h1>Mi nombre es José Luis García</h1>"

@app.route("/lenguajes-de-programacion") # http://127.0.0.1:5000/lenguajes-de-programacion
def lenguajes():
    return """
    <h1>Lenguajes de programación</h1>
    <p>Python</p>
    <p>Java</p>
    <p>JavaScript</p>
    <p>C++</p>
    <p>C#</p>
    """



if __name__ == '__main__':
    app.run()
