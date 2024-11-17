numero = int(input("Introduce un numero entero positivo:"))
factores = []

for dk in range(1, numero + 1):
    if numero % dk == 0:
        factores.append(dk)

print("factores de", numero, ":", factores)