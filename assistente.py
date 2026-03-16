import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")

class TheWalkingDead:

    def buscar_serie(self, nome):
        url = f"http://www.omdbapi.com/?t={nome}&apikey={API_KEY}"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()

            return {
                "titulo": dados.get("Title"),
                "ano": dados.get("Year"),
                "genero": dados.get("Genre"),
                "nota_imdb": dados.get("imdbRating"),
                "sinopse": dados.get("Plot")
            }

        return {"erro": "Série não encontrada"}