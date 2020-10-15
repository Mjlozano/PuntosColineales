import matplotlib.pyplot as plt
from Colineal import Colineal
from Colineal import SegmentoDeLinea
from Punto import Punto

# fileName = input("Ingrese nombre del archivo>>>  ")

fileName = "puntos.txt"

# Se manda el nombre del archivo para poder ser manipulado
puntosColineales = Colineal(fileName)
puntosColineales.dibujar()
