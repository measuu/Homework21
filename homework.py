import requests
import flask
from flask import Flask, redirect, jsonify
import random

app = Flask(__name__)

@app.route("/")
def welcome():
    return redirect("/crypto")

@app.route("/crypto")
def crypt():
    data = requests.get("https://dogapi.dog/api/v2/breeds")
    response = data.json()
    data1 = response['data']
    breed = random.sample(data1, 1)
    return jsonify(breed)

if __name__=="__main__":
    app.run(debug=True)

