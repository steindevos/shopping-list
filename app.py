import os
from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "ci-project"
app.config["MONGO_URI"] = "mongodb://Admin:chocoladet55rt@ds161411.mlab.com:61411/ci-project"

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True
    )