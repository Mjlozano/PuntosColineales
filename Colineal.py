from Punto import Punto
from Linea import Linea
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
            tempPoint = Punto(int(pt[0]), int(pt[1]))
            listaPuntos.append(tempPoint)
        return listaPuntos

    def dibujar(self):
        linea = SegmentoDeLinea(self.getPoints())

        # devuelve todos los conjuntos colineales
        linea.esColineal()

        for i in linea.esColineal():
            for j in i.puntos:
                plt.plot([j.x], [j.y], "ro-")
        plt.show()


class SegmentoDeLinea:
    def __init__(self, listaDePuntos):
        self.listaDePuntos = listaDePuntos

    def pendiente(self, y1, y0, x1, x0):
        return (y1 - y0) / (x1 - x0)

    # Verica si los puntos dados son colineales
    def collinear(self, a, b, c):
        return (b.x - a.x) * (c.y - a.y) == (c.x - a.x) * (b.y - a.y)

    def esColineal(self):
        tempList = []
        conjuntoColineal = []
        inicial = 0
        i = 1
        while i <= len(self.listaDePuntos):
            if (i + 1) == len(self.listaDePuntos):
                inicial += 1
                i = inicial + 1
            if i >= 1 and (i + 1) <= len(self.listaDePuntos) - 1:
                p1 = self.listaDePuntos[inicial]
                p2 = self.listaDePuntos[i]
                p3 = self.listaDePuntos[i + 1]
                if self.collinear(p1, p2, p3):
                    linea = Linea(p1, p2, p3)
                    tempList.append(linea)
            i += 1

        for val in tempList:
            if val != None:
                conjuntoColineal.append(val)

        return conjuntoColineal
