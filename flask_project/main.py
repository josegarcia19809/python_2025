from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Aprendiendo Flask"

@app.route("/informacion")
def informacion():
    return "<h1>Página de información</h1>"



if __name__ == '__main__':
    app.run()
