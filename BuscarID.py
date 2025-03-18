import requests
import json
import tkinter as tk
from tkinter import ttk, messagebox

def buscar_anime_por_id(anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"
    response = requests.get(url, headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def exibir_anime(anime_data):
    if anime_data:
        formatted_data = json.dumps(anime_data, indent=4, ensure_ascii=False)
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, formatted_data)
    else:
        messagebox.showerror("Erro", "Não foi possível buscar os dados do anime.")

def buscar_anime():
    anime_id = entry_id.get()
    anime_data = buscar_anime_por_id(anime_id)
    exibir_anime(anime_data)

# Configuração da janela principal
root = tk.Tk()
root.title("Busca de Anime por ID")
root.geometry("800x600")

# Configuração do estilo
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

# Widgets
label_id = ttk.Label(root, text="Digite o ID do anime:")
label_id.pack(pady=10)

entry_id = ttk.Entry(root, font=("Helvetica", 12))
entry_id.pack(pady=10)

button_buscar = ttk.Button(root, text="Buscar", command=buscar_anime)
button_buscar.pack(pady=10)

text_widget = tk.Text(root, wrap="word", font=("Helvetica", 10))
text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Inicia a aplicação
root.mainloop()