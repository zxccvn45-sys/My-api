from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DB_FILE = "users.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return "API Running ✅"

@app.route("/validate", methods=["POST"])
def validate():
    key = request.json.get("key")
    data = load_data()

    for user in data:
        if key in data[user]["keys"]:
            return jsonify({"status": "valid"})

    return jsonify({"status": "invalid"})

@app.route("/add_key", methods=["POST"])
def add_key():
    user_id = str(request.json.get("user_id"))
    key = request.json.get("key")

    data = load_data()

    if user_id not in data:
        data[user_id] = {"keys": []}

    data[user_id]["keys"].append(key)
    save_data(data)

    return jsonify({"status": "added"})from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DB_FILE = "users.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return "API Running ✅"

@app.route("/validate", methods=["POST"])
def validate():
    key = request.json.get("key")
    data = load_data()

    for user in data:
        if key in data[user]["keys"]:
            return jsonify({"status": "valid"})

    return jsonify({"status": "invalid"})

@app.route("/add_key", methods=["POST"])
def add_key():
    user_id = str(request.json.get("user_id"))
    key = request.json.get("key")

    data = load_data()

    if user_id not in data:
        data[user_id] = {"keys": []}

    data[user_id]["keys"].append(key)
    save_data(data)

    return jsonify({"status": "added"})
    
