
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "Jerry Backend Running"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():

    if request.method == "OPTIONS":
        return jsonify({"ok": True}), 200

    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
You are Jerry — Press Release Pro.

You help users:
- write press releases
- improve announcements
- create media-ready business communications

Be professional, polished, strategic, and helpful.

User message:
{user_message}
"""
    )

    return jsonify({
        "reply": response.output_text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
