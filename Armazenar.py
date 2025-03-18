import pandas as pd

def criar_dataframe(animes):
    dados = []
    for anime in animes:
        dados.append({
            'id': anime.get('mal_id'),
            'titulo': anime.get('title'),
            'sinopse': anime.get('synopsis'),
            'generos': [genero['name'] for genero in anime.get('genres', [])],
            'pontuacao': anime.get('score')
        })
    return pd.DataFrame(dados)

animes = []  # Define an empty list or populate it with anime data
df_animes = criar_dataframe(animes)
print(df_animes.head())
