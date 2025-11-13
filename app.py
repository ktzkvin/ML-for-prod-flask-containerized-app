"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import os
import json
from flask import Flask, render_template
from pymongo import MongoClient

##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

##########################################################################
## Routes
##########################################################################

@app.route("/")
def home():
    col = MongoClient("mongodb://mongo:27017")["testdb"]["restaurants"]
    path = "data/restaurant.json"

    docs = [json.loads(line) for line in open(path)]
    col.drop()
    col.insert_many(docs)

    return render_template("home.html", restaurants=list(col.find()))

##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()
