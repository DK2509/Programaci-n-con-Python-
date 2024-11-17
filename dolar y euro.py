i = input("ingrese lo que quiere convertir a peso dominicano:")
if i == "dolar":
    numero = int(input("ingrese la cantidad de dinero que desea convertir a peso dominicano:"))
    dolar = numero * 60.42
    resultado = dolar
    print(f"su cantidad de {i} son: {resultado}")

elif i == "euro":
    numero = int(input("ingrese la cantidad de dinero que desea convertir a peso dominicano:"))
    dolar = numero * 63.73
    resultado = dolar
    print(f"su cantidad de {i} son: {resultado}")
