#!/usr/bin/python
from flask import Flask, render_template, request, Response
import sqlite3
import json

app = Flask(__name__)

@app.route("/")
def select():
    connection = sqlite3.connect("control.db")
    cursor = connection.cursor()
    cursor.execute("SELECT datetime , TemperatureC , CPU  from Temperature")
    results = cursor.fetchall()
    print(results)
    return Response(json.dumps(results), mimetype='application/json') #jsonify(json.loads(results)) #json.dumps(results)

@app.route("/graph")
def graph():
    return render_template('MultiY.html')


if __name__ == '__main__':
    app.run(
    debug=True,
    threaded=True,
    host='0.0.0.0',
    port=5000
)
