from Colineal import Colineal

print("_____________________________________________\n")
fileName = input("Ingrese nombre del archivo:  ")

# Se manda el nombre del archivo para poder ser manipulado
puntosColineales = Colineal(fileName)

puntosColineales.dibujar()
