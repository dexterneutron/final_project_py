from flask import Flask, jsonify
from lib.storedata import get_data

app = Flask(__name__)

@app.route("/api/feed", methods = ['GET'])
def retrive_data():
    data = get_data()
    return jsonify(data)


