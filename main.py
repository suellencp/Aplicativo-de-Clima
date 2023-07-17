# Importar as bibliotecas necessárias
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

# Função para obter as informações de clima do OpenWeatherMap API
def get_weather(city):
    API_key = "e23e39351f11d4943bbb868255599c78"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Erro", "Cidade não encontrada")
        return None
    
    # Analisa a resposta JSON para obter informações meteorólogicas
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # Obtém o URL do ícone e retorna todas as informações meteorológicas
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# Função para pesquisar o tempo/clima para uma cidade
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # Se a cidade for encontrada, descompacte as informações do clima/tempo
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    # Obtém a imagem do ícone do clima no URL e atualiza o rótulo do ícone
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Atualiza os rótulos de temperatura e descrição
    temperature_label.configure(text=f"Temperatura: {temperature:.2f}°C")
    description_label.configure(text=f"Descrição: {description}")

root = ttkbootstrap.Window(themename="morph")
root.title("Previsão do Tempo")
root.geometry("400x400")

# Entrada de nomes da cidade
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Botão para procurar informações do c lima
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Mostrar o nome da cidade/país
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# Mostrar o ícone do tempo
icon_label = tk.Label(root)
icon_label.pack()

# Mostrar a temperatura
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()
 
# Mostrar a descrição do clima/tempo
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()