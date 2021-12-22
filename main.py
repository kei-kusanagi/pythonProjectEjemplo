from flask import Flask, render_template

app = Flask(__name__)


@app.route("pythonprojectejemplo.herokuapp.com")
def inicio():
    return render_template("index.html")



