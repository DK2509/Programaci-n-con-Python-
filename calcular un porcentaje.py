print("coloque el porcentaje que desea calcular:")
valor = float(input())
print("ingrese el numero base:")
numero = float(input())
resultado = valor * numero / 100
print("El", valor, "porciento de", numero, "es", round(resultado, 2))