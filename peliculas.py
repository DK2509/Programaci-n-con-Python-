peliculas = []

while True:
    pelicula = input("¿cuales peliculas te gustan?:")
    if pelicula == "solo esas":
        break
    else:
        peliculas.append(pelicula)

for pelicula in peliculas:
    print("te gusta:", pelicula)
