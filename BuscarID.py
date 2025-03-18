import requests

anime_id = 52991

def buscar_anime_por_id(anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"
    response = requests.get(url, headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    anime_id = input("Digite o ID do anime: ")
    anime_data = buscar_anime_por_id(anime_id)
    
    if anime_data:
        print(anime_data)
    else:
        print("Não foi possível buscar os dados do anime.")

if __name__ == "__main__":
    main()