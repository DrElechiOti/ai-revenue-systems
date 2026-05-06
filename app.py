
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Revenue System Backend Running"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return jsonify({"ok": True}), 200

    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")

    return jsonify({
        "reply": f"Jerry received: {user_message}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
