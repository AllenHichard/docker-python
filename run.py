from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return 'Ola, estou na aplicação setada'


from src import UserRepo
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return 'Ola, estou na aplicação setada'


@app.route("/insert", methods=["POST"])
def insert():
    userRepo = UserRepo()
    body = request.json

    userRepo.insert_user(body["name"])

    return 'OK'

#host="0.0.0.0")
#$env:FLASK_APP="run.py"
#flask run
#python3 -m flask run --host=0.0.0.0"