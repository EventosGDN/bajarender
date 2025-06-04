from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/reflexion", methods=["POST"])
def reflexion():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Mensaje vacío"}), 400

    # Tu lógica real, podés reemplazar esta respuesta dummy si hace falta
    respuesta = f"🌿 Gracias por compartir eso. No estás solo/a. Lo que sentís importa."

    return jsonify({ "response": respuesta })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
