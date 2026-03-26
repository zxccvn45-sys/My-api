from flask import Flask, request, jsonify
import json, random, string, os

app = Flask(__name__)
DB_FILE = "users.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_key():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(32))

@app.route("/")
def home():
    return "API is running"

@app.route("/generate")
def generate():
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    data = load_data()

    if user_id not in data:
        data[user_id] = {"keys": []}

    new_key = generate_key()
    data[user_id]["keys"].append(new_key)

    save_data(data)

    return jsonify({"api_key": new_key})

@app.route("/check")
def check():
    key = request.args.get("key")

    if not key:
        return jsonify({"error": "key required"}), 400

    data = load_data()

    for user in data:
        if key in data[user]["keys"]:
            return jsonify({"status": "valid"})

    return jsonify({"status": "invalid"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
