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
    path = os.path.join(os.path.dirname(__file__), "data", "restaurant.json")

    docs = []
    for line in open(path, encoding="utf-8"):
        d = json.loads(line)
        d.pop("_id", None)
        docs.append(d)

    col.drop()
    col.insert_many(docs)

    restaurants = list(col.find({}, {"_id": 0}))
    return render_template("home.html", restaurants=restaurants)


##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()
