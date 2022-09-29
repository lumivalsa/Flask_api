from crypt import methods
from logging import exception
from Models import db, medios
import json
from flask import Flask, request, jsonify, render_template
import sqlite3
import os

os.chdir(os.path.dirname(__file__))
app= Flask(__name__)

app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Bienvenido al programa de predicción de datos de venta </h1>"

@app.route('/data', methods=['GET'])
def get_all():
    connection = sqlite3.connect('data/datos.db')
    cursor = connection.cursor()
    select_datos = "SELECT * FROM datos"
    result = cursor.execute(select_datos).fetchall()
    connection.close()
    return jsonify(result)

@app.route("/ingest_data")
def ingresa():
    return render_template("index.html")

@app.route("/api/adddatos", methods=['POST'])
def adddatos():
    connection = sqlite3.connect('data/datos.db')
    cursor = connection.cursor()
    TV= request.form["TV"]
    radio= request.form["radio"]
    newspaper=request.form["newspaper"]
    sales= request.form["sales"]
    agrega_datos = """
    INSERT INTO datos VALUE(TV,radio,newspaper,sales);
    """
    cursor.executescript(agrega_datos)
    result = cursor.execute(agrega_datos).fetchall()
    connection.close()
    return jsonify(result)





app.run()