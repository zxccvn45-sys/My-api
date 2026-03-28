from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DB_FILE = "users.json"

# Load data safely
def load_data():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# Save data
def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Home route
@app.route("/")
def home():
    return "API Running ✅"

# 1️⃣ Validate key
@app.route("/validate", methods=["POST"])
def validate():
    key = request.json.get("key")
    data = load_data()

    for user in data:
        if key in data[user]["keys"]:
            return jsonify({"status": "valid"})

    return jsonify({"status": "invalid"})

# 2️⃣ Add key
@app.route("/add_key", methods=["POST"])
def add_key():
    user_id = str(request.json.get("user_id"))
    key = request.json.get("key")

    data = load_data()

    if user_id not in data:
        data[user_id] = {"keys": []}

    data[user_id]["keys"].append(key)
    save_data(data)

    return jsonify({"status": "added", "key": key})

# 3️⃣ Delete key
@app.route("/delete_key", methods=["POST"])
def delete_key():
    user_id = str(request.json.get("user_id"))
    key = request.json.get("key")

    data = load_data()

    if user_id in data and key in data[user_id]["keys"]:
        data[user_id]["keys"].remove(key)
        save_data(data)
        return jsonify({"status": "deleted"})

    return jsonify({"status": "not_found"})

# 4️⃣ List keys
@app.route("/list_keys", methods=["POST"])
def list_keys():
    user_id = str(request.json.get("user_id"))
    data = load_data()

    if user_id in data:
        return jsonify({"keys": data[user_id]["keys"]})

    return jsonify({"keys": []})

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
