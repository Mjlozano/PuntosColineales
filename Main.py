from Colineal import Colineal
from Colineal import SegmentoDeLinea

fileName = input("Ingrese nombre del archivo>>>  ")

# Se manda el nombre del archivo para poder ser manipulado
puntosColineales = Colineal(fileName)

puntosColineales.dibujar()
