import requests

def obtener_Personajes(): # definimos la funcion para obtener respuestas get de la api
    url = "https://api.disneyapi.dev/character"  # la url de la api a utilizar
    respuesta = requests.get(url)  #hacemos la solicitud get a nuestra url api
    # Verficamos el estatus de la solicitud, una respuesta 200 significa exito!  
    if respuesta.status_code == 200: 
        return respuesta.json() #Guardamos en un json
    else:
        return None 

def mostrar_personaje(personaje): #Mostrramos los personajes y sus datos.
    print("\nNombre:", personaje['name'])
    print("Películas:", ', '.join(personaje['films']))
    print("Series de TV:", ', '.join(personaje['tvShows']))
    print("Videojuegos:", ', '.join(personaje['videoGames']))
    print("URL de origen:", personaje['sourceUrl'])
    print("Imagen:", personaje['imageUrl'])

    personajes = obtener_Personajes() # Obtenemos los personajes de la API

    if personajes is not None: # Verificamos si la respuesta de la API es válida
        lista_personajes = personajes['data'] # Extraemos la lista de personajes de los datos obtenidos

        # Iteramos sobre cada personaje en la lista, enumerando desde 1
        for i, personaje in enumerate(lista_personajes, start=1):
            print(f"\nPersonaje {i}:")
            mostrar_personaje(personaje)# Mostramos el nombre y los detalles del personaje actual
             # Preguntamos al usuario si desea ver más personajes
            respuesta = input("\n¿Quieres ver más personajes? (s/n): ").strip().lower()
            if respuesta != 's': # Si la respuesta no es 's', salimos del bucle
                break
    else: # Si hubo un error al usar la API, mostramos un mensaje de error
        print("Hubo un error al usar la API")
