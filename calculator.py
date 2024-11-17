o = input("escriba el operador que desea usar:")

if o == "suma":
    valor1 = int(input("ingrese el primer numero:"))
    valor2 = int(input("ingrese el segundo numero:"))
    resultado = valor1 + valor2
    print(f"el resultado de la {o} es: {resultado}")

elif o == "resta":
    valor1 = int(input("ingrese el primer numero:"))
    valor2 = int(input("ingrese el segundo numero:"))
    resultado = valor1 - valor2
    print(f"el resultado de la {o} es: {resultado}")

elif o == "multiplicar":
    valor1 = int(input("ingrese el primer numero:"))
    valor2 = int(input("ingrese el segundo numero:"))
    resultado = valor1 * valor2
    print(f"el resultado de la {o} es: {resultado}")

elif o == "dividir":
    valor1 = int(input("ingrese el primer numero:"))
    valor2 = int(input("ingrese el segundo numero:"))
    resultado = valor1 / valor2
    print(f"el resultado de la {o} es: {resultado}")

elif o == "exponente":
    valor1 = int(input("ingrese el primer numero:"))
    valor2 = int(input("ingrese el numero al que lo desea elevar:"))
    resultado = valor1 ** valor2
    print(f"el resultado de la {o} es: {resultado}")
