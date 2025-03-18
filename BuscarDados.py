import requests

def buscar_animes(pagina=1, limite=25):
    url = f"https://api.jikan.moe/v4/anime?page={pagina}&limit={limite}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()['data']
    else:
        print("Erro na requisição:", resposta.status_code)
        return []

# Teste a função
animes = buscar_animes()
for anime in animes:
    print(anime['title'], "-", anime['score'])
