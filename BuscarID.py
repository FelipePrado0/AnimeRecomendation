import requests
from bs4 import BeautifulSoup
import json
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

def buscar_id_anime_por_nome(nome_anime):
    search_url = f"https://myanimelist.net/search/all?q={nome_anime.replace(' ', '%20')}"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find('a', class_='hoverinfo_trigger fw-b fl-l')
        if result:
            anime_url = result['href']
            anime_id = anime_url.split('/')[-2]
            return anime_id
    return None

def buscar_anime_por_id(anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"
    response = requests.get(url, headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

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

def exibir_anime(anime_data):
    if anime_data:
        formatted_data = json.dumps(anime_data, indent=4, ensure_ascii=False)
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, formatted_data)
    else:
        messagebox.showerror("Erro", "Não foi possível buscar os dados do anime.")

def buscar_anime():
    nome_anime = entry_nome.get()
    anime_id = buscar_id_anime_por_nome(nome_anime)
    if anime_id:
        anime_data = buscar_anime_por_id(anime_id)
        exibir_anime(anime_data)
        
        if anime_data:
            df_animes = criar_dataframe([anime_data['data']])
            print(df_animes.head())
            # Salvar o DataFrame em um arquivo CSV
            df_animes.to_csv('animes.csv', index=False)
    else:
        messagebox.showerror("Erro", "Não foi possível encontrar o ID do anime.")

# Configuração da janela principal
root = tk.Tk()
root.title("Busca de Anime por Nome")
root.geometry("800x600")

# Configuração do estilo
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

# Widgets
label_nome = ttk.Label(root, text="Digite o nome do anime:")
label_nome.pack(pady=10)

entry_nome = ttk.Entry(root, font=("Helvetica", 12))
entry_nome.pack(pady=10)

button_buscar = ttk.Button(root, text="Buscar", command=buscar_anime)
button_buscar.pack(pady=10)

text_widget = tk.Text(root, wrap="word", font=("Helvetica", 10))
text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Inicia a aplicação
root.mainloop()