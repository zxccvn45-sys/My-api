from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# In-memory storage for user API keys
# Format: {user_id: api_key}
api_keys = {}

# ===== GENERATE =====
@app.route("/generate")
def generate():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    # Generate a random 32-character hex API key
    key = secrets.token_hex(16)  # 32 characters
    api_keys[user_id] = key

    return jsonify({"api_key": key})

# ===== CHECK =====
@app.route("/check")
def check():
    key = request.args.get("key")
    if not key:
        return jsonify({"error": "Missing key"}), 400

    # Find if key exists in storage
    if key in api_keys.values():
        return jsonify({"status": "valid"})
    return jsonify({"status": "invalid"})

# ===== HEALTH CHECK =====
@app.route("/")
def home():
    return "API is running!"

# ===== RUN SERVER =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
