import tkinter as tk
from tkinter import ttk

def abrir_buscar_por_nome():
    from src import BuscarID
    BuscarID.main()

def abrir_buscar_por_descricao():
    from src import BuscarDescricao
    BuscarDescricao.main()

def abrir_buscar_por_recomendacao():
    from src import BuscarRecomendacao
    BuscarRecomendacao.main()

def abrir_buscar_por_genero():
    from src import BuscarGenero
    BuscarGenero.main()

def abrir_buscar_por_nota():
    from src import BuscarNota
    BuscarNota.main()

# Configuração da janela principal
root = tk.Tk()
root.title("Menu de Busca de Animes")
root.geometry("400x300")

# Configuração do estilo
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

# Widgets
label_menu = ttk.Label(root, text="Escolha uma opção de busca:")
label_menu.pack(pady=20)

button_nome = ttk.Button(root, text="Buscar Anime por Nome", command=abrir_buscar_por_nome)
button_nome.pack(pady=10)

button_descricao = ttk.Button(root, text="Buscar Anime por Descrição", command=abrir_buscar_por_descricao)
button_descricao.pack(pady=10)

button_recomendacao = ttk.Button(root, text="Buscar Anime por Recomendação", command=abrir_buscar_por_recomendacao)
button_recomendacao.pack(pady=10)

button_genero = ttk.Button(root, text="Buscar Anime por Gênero", command=abrir_buscar_por_genero)
button_genero.pack(pady=10)

button_nota = ttk.Button(root, text="Buscar Anime por Nota", command=abrir_buscar_por_nota)
button_nota.pack(pady=10)

# Inicia a aplicação
root.mainloop()