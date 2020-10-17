from Colineal import Colineal
import os


# Este metodo es para limpiar la consola y asi limpiar
# el texto de la ejecución anterior
def cls():
    os.system("cls" if os.name == "nt" else "clear")


cls()

try:
    # Se manda el nombre del archivo para poder ser manipulado
    fileName = input("Ingrese nombre del archivo:  ")
    puntosColineales = Colineal(fileName)
    puntosColineales.dibujar()
except:
    print("--------------------------------")
    print("El archivo que ingresó no existe")
    print("--------------------------------")
