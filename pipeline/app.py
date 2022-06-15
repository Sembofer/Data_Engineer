from flask import Flask, request
from task_db import query

app = Flask(__name__)


@app.route('/tasks', methods = ['POST'])
def task_query():
    activity = request.json['requirement']
    data = request.json['id']
    return query(activity, data)

if __name__  == '__main__':
    app.run(debug=True)