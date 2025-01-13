import requests
from bs4 import BeautifulSoup

url = "https://vandal.elespanol.com/rankings/game-boy-advance"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, "html.parser")
    juegos = soup.find_all("table", class_="table transparente tablasinbordes")

    for juego in juegos:
        id = juego.find("b").text.strip()
        calificacion = juego.find("div", class_="circuloanalisis_saga mauto").find("a").text.strip()
        nombre = juego.find("td", class_="ta14b t11").find("a").text.strip()
        imagen = juego.find("div", class_="relative wrapper_imgabsoluta").find("a").find("img")["data-src"]
        print(f"id: {id}\nnombre: {nombre}\nimagen: {imagen}\ncalificacion: {calificacion}\n")
else:
    print(f"hubo un error en la peticion, {respuesta.status_code}")
