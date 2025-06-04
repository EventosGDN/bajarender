# app.py
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct"

@app.route("/reflexion", methods=["POST"])
def modo_reflexion():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "Missing message"}), 400

    messages = [
        {"role": "system", "content": (
            "Sos un amigo psicólogo con una mirada empática, realista y contenedora. "
            "Tu objetivo es ayudar al usuario a entender lo que siente, responder con lógica, "
            "ser directo cuando es necesario, y cuidar emocionalmente su bienestar."
        )},
        {"role": "user", "content": user_input}
    ]

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://tu-app.com",
        "X-Title": "BajaUnCambioReflexion"
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": reply})
    else:
        return jsonify({"error": "Failed to fetch response from model.", "details": response.text}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
