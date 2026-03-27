from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage of API keys (for demonstration)
api_keys = {}

# ===== GENERATE =====
@app.route("/generate")
def generate():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    # Create a simple API key
    key = f"key_for_{user_id}"
    api_keys[user_id] = key
    return jsonify({"api_key": key})

# ===== CHECK =====
@app.route("/check")
def check():
    key = request.args.get("key")
    if not key:
        return jsonify({"error": "Missing key"}), 400

    # Check if the key is valid
    if key in api_keys.values():
        return jsonify({"status": "valid"})
    else:
        return jsonify({"status": "invalid"})

# ===== HEALTH CHECK =====
@app.route("/")
def home():
    return "API is running!"

# ===== RUN SERVER =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
