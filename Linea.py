class Linea:
    def __init__(self, *argv):
        lines = []
        for arg in argv:
            lines.append(arg)
        self.puntos = lines

    def showLines(self):
        for point in self.puntos:
            print(point)
