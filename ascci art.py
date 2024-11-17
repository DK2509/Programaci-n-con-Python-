#tener en cuenta que debes descargar pyfiglet para poder ejecutar el programa.
import pyfiglet
titulo = input("ingrese la palabra u oracion que desea graficar:")
grafico = pyfiglet.figlet_format(titulo)
print(grafico)