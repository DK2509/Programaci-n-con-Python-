print("Hola. Espero y se encuentre bien.")
print("Para clasificar el sueldo necesitamos saber cuanto gana al año")
sueldo = int(input("ingrese el sueldo anual:"))

if sueldo >= 50_000_000:
    print("Consigues una buena cantidad de dinero al año")
elif sueldo >= 10_000_000:
    print("usted esta en condiciones de tener una buena vida")
elif sueldo >= 1_000_000:
    print("usted puede llegar a tener una vida razonable")
elif sueldo >= 500_000:
    print("sus ingresos son considerables")
elif sueldo >= 100_000:
    print("sus ingresos son algo bajos")
elif sueldo >= 50_000:
    print("sus ingresos anuales son muy bajos")

print("Dependiendo de la capacidad de dinero colocada se le clasifico")