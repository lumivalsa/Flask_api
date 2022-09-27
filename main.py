from flask import Flask, request, jsonify
import os
import pickle
import pandas as pd
from sklearn.model_selection import cross_val_score

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a mi API del modelo advertising"
