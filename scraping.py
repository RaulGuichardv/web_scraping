import requests
import csv
from bs4 import BeautifulSoup

url = "https://vandal.elespanol.com/rankings/game-boy-advance"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, "html.parser")
    juegos = soup.find_all("table", class_="table transparente tablasinbordes")


    with open("salida.csv", "w", newline="", encoding="utf-8") as file:
        encabezado = ["id", "nombre", "imagen", "calificacion"]
        escritor = csv.DictWriter(file, fieldnames=encabezado)
        escritor.writeheader()

        for juego in juegos:
            try:
                id = juego.find("b").text.strip() if juego.find("b") else "N/A"
                calificacion = juego.find("div", class_="circuloanalisis_saga mauto").find("a").text.strip() if juego.find("div", class_="circuloanalisis_saga mauto") else "N/A"
                nombre = juego.find("td", class_="ta14b t11").find("a").text.strip() if juego.find("td", class_="ta14b t11") else "N/A"
                imagen = juego.find("div", class_="relative wrapper_imgabsoluta").find("a").find("img")["data-src"] if juego.find("div", class_="relative wrapper_imgabsoluta") else "N/A"

                print(f"id: {id}\nnombre: {nombre}\nimagen: {imagen}\ncalificacion: {calificacion}\n")

                dict_juego = {
                    "id": id,
                    "nombre": nombre,
                    "imagen": imagen,
                    "calificacion": calificacion
                }
                escritor.writerow(dict_juego)  # Escribimos una fila en el CSV

            except AttributeError:
                print("Error al extraer datos de un juego, posiblemente faltan elementos.")

else:
    print(f"Hubo un error en la petición, código: {respuesta.status_code}")