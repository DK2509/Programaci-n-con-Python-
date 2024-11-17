print("Nos gustaria saber como conociste el mundo de la programacion")
familiar = input("¿tienes algun familiar que este relacionado con esto?:")
if familiar == "si":
    a = input("¿Que area de la programacion este se especializa?:")
    input("Entiendo")
    input("¿Tiene mucho tiempo relacionado con eso?:")
    print("Esta bien.")
elif familiar == "no":
    input("En ese caso. ¿Como conociste la progrmacion?:")
    print("Esta bien")
    b = input("¿Has hecho cursos de programacion?:")
    if b == "si":
        cursos = int(input("Cuantos cursos has hecho?:"))
        if cursos >= 3:
            input("Por lo que dices veo y ya estas algo informado de lo que es este mundo")
            print("Gracias por su tiempo..")
        elif cursos < 2:
            print("Por lo que dices eres algo nuevo en lo que es este mundo.")
            print("Es bueno que sigas practicando lo que ya sabes y mejorando tus conocimientos.")
    elif b == "no":
        print("Es bueno que si te gusta la programacion o te llame la atencion")
        print("Hagas cursos y te informes mucho de la programacion y puedas algun dia sacarle provecho a eso")