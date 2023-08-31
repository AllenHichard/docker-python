from flask import Flask, request
from src import UserRepo

app = Flask(__name__)


@app.route("/insert", methods=["POST"])
def insert():
    userRepo = UserRepo()
    body = request.json
    userRepo.insert_user(body["name"])
    return 'sucess'
