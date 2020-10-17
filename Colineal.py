from Punto import Punto
from Linea import Linea
from itertools import combinations
import matplotlib.pyplot as plt


class Colineal:
    def __init__(self, fileName):
        self.fileName = fileName
        self.pointsFile = open(fileName, "r")
        self.line = self.pointsFile.readlines()

    ##Se obtiene la lista de puntos que está en el archivo
    def getFilePoints(self):
        points = map(lambda x: x.rstrip(), self.line)
        return list(points)

    def getPoints(self):
        listaPuntos = []
        p = self.getFilePoints()
        del p[0]
        for i in p:
            pt = i.split()
            tempPoint = Punto(float(pt[0]), float(pt[1]))
            listaPuntos.append(tempPoint)
        return listaPuntos

    def dibujar(self):
        linea = SegmentoDeLinea(self.getPoints())

        # grafica los puntos no colineales
        for p in self.getPoints():
            plt.plot([p.x], [p.y], "ro-")

        # grafica los puntos colineales con sus lineas
        for i in linea.esColineal():

            plt.plot(
                [i.puntos[0].x, i.puntos[1].x, i.puntos[2].x],
                [i.puntos[0].y, i.puntos[1].y, i.puntos[2].y],
                "ro-",
            )
        plt.show()


class SegmentoDeLinea:
    def __init__(self, listaDePuntos):
        self.listaDePuntos = listaDePuntos

    # Verica si los puntos dados son colineales
    def collinear(self, a, b, c):
        return (b.x - a.x) * (c.y - a.y) == (c.x - a.x) * (b.y - a.y)

    def esColineal(self):
        # Genera todos las combinaciones posibles de conjuntos de 3 puntos
        comb = combinations(self.listaDePuntos, 3)
        print(len(comb))
        conjuntoColineal = []
        for item in comb:
            p1, p2, p3 = item[0], item[1], item[2]
            if self.collinear(p1, p2, p3):
                linea = Linea(p1, p2, p3)
                conjuntoColineal.append(linea)
        return conjuntoColineal
