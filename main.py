from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Perguntas de exemplo
quiz_data = [
    {"id": 1, "pergunta": "Qual a capital do Brasil?", "opcoes": ["São Paulo", "Brasília", "Rio de Janeiro"], "resposta": "Brasília"},
    {"id": 2, "pergunta": "Quanto é 2 + 2?", "opcoes": ["3", "4", "5"], "resposta": "4"},
    {"id": 3, "pergunta": "Qual linguagem usamos com Flet?", "opcoes": ["Java", "Python", "C++"], "resposta": "Python"},
    {"id": 4, "pergunta": "teste", "opcoes": ["teste1", "Python", "C++"], "resposta": "teste1"}
]

@app.route("/perguntas", methods=["GET"])
def get_perguntas():
    return jsonify(quiz_data)

@app.route("/verificar", methods=["POST"])
def verificar_resposta():
    data = request.json
    pergunta_id = data["id"]
    resposta = data["resposta"]

    for pergunta in quiz_data:
        if pergunta["id"] == pergunta_id:
            correta = pergunta["resposta"] == resposta
            return jsonify({"correta": correta})

    return jsonify({"erro": "Pergunta não encontrada"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
