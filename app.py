
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Revenue System Backend Running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    return jsonify({
        "reply": f"You said: {message}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
