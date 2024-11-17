print("Si desea solicitar cedula de identidad necesitamos saber su edad")
v = int(input("Introdude tu edad:"))

if v >= 18:
    print("Usted puede tener cedula de identidad")

elif v < 18:
    print("Usted no puede tener cedula de identidad")