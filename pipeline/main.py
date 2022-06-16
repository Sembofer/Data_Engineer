from flask import Flask, request
from etl_process import Stackoverflow
from cfg import DB_CONNSTR, URL
from task_db import task_query

Stackoverflow(URL).load_data(DB_CONNSTR)




app = Flask(__name__)

@app.route('/', methods = ['POST'])
def query():
    requirement = request.json['requirement']
    data = request.json['id']
    return task_query(requirement, data)



if __name__ == "__main__":
    app.run(debug=True)