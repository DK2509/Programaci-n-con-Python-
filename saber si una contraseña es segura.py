contraseña=False

for dk in input("escribe una contraseña:"):
    if dk==("@" or "/" or "_" or "?" or "#" or "*"):
        contraseña=True

if contraseña==True:
    print("su contraseña es segura")
else:
    print(("La contraseña no es muy segura..."))