from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return 'Ola, estou na aplicação setada'

#host="0.0.0.0")
#$env:FLASK_APP="run.py"
#flask run
#python3 -m flask run --host=0.0.0.0"