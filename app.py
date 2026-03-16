from flask import Flask, jsonify
from assistente import TheWalkingDead

app = Flask(__name__)
assistente = TheWalkingDead()

@app.route("/")
def home():
    series = ["The Walking Dead", "Breaking Bad", "Stranger Things"]
    resultados = [assistente.buscar_serie(serie) for serie in series]
    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)
