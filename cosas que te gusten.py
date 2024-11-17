print("Hola. Nos gustaria saber cuatro cosas te gustan")
n = input("¿Te gustaria decirme?")
if n == "si":
    a = input("Cuentame de algo que te guste:")
    b = input("Cuentanos sobre algo mas que te guste:")
    c = input("Aparte de eso ¿Cuales otras cosas te gustan?")
    d = input("¿Que mas te gusta?:")
    print("entonces te gustan:")
    print(a)
    print(b)
    print(c)
    print(d)

elif n == "no":
    print("Bueno. Disculpe las molestias.")
