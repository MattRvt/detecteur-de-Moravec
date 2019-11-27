import time
from concurrent.futures import thread
from multiprocessing import Process


class Partie(Process):
    # """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, minY, maxY, im, h, w, i, queue):
        Process.__init__(self)

        self.queue = queue
        self.minY = minY
        self.maxY = maxY
        self.im = im
        self.h = h
        self.w = w
        self.i = i
        self.imIntensite = [[0 for j in range(w)] for i in range(h)]

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        for y in range(self.minY, self.maxY):
            for x in range(self.w):
                rayonVoisinageStatic = 5
                rayonVoisinage = rayonVoisinageStatic
                voisinageParcourue = False
                intensitePixeles = 0
                p = self.im[y][x]
                somme = 0
                while not voisinageParcourue:
                    n = 0
                    # si on atteint le pas bord en bas de l'immage
                    if (y - rayonVoisinage >= 0):
                        # px du haut
                        somme = somme + self.Intensite(self.im[y - rayonVoisinage][x][0],
                                                       self.im[y - rayonVoisinage][x][1],
                                                       self.im[y - rayonVoisinage][x][2])
                        n = n + 1
                        if (x - rayonVoisinage >= 0):
                            # haut gauche
                            for i in range(x - rayonVoisinage, x):
                                somme = somme + self.Intensite(self.im[y - rayonVoisinage][x - i][0],
                                                               self.im[y - rayonVoisinage][x - i][1],
                                                               self.im[y - rayonVoisinage][x - i][2])
                                n = n + 1
                            # haut droit
                        if (x + rayonVoisinage < self.w):
                            for i in range(x + 1, x + rayonVoisinage + 1):
                                somme = somme + self.Intensite(self.im[y - rayonVoisinage][x + rayonVoisinage][0],
                                                               self.im[y - rayonVoisinage][x + rayonVoisinage][1],
                                                               self.im[y - rayonVoisinage][x + rayonVoisinage][2])
                                n = n + 1
                    #   si on atteint pas la limite haut de l'image
                    if (y + rayonVoisinage < self.h):
                        # px du bas
                        somme = somme + self.Intensite(self.im[y + rayonVoisinage][x][0],
                                                       self.im[y + rayonVoisinage][x][1],
                                                       self.im[y + rayonVoisinage][x][2])
                        n = n + 1
                        if (x - rayonVoisinage >= 0):
                            # bas gauche
                            for i in range(x - rayonVoisinage, x):
                                somme = somme + self.Intensite(self.im[y + rayonVoisinage][x - rayonVoisinage][0],
                                                               self.im[y + rayonVoisinage][x - rayonVoisinage][1],
                                                               self.im[y + rayonVoisinage][x - rayonVoisinage][2])
                                n = n + 1
                            # bas droit
                        if (x + rayonVoisinage < self.w):
                            for i in range(x + 1, x + rayonVoisinage + 1):
                                somme = somme + self.Intensite(self.im[y + rayonVoisinage][x + rayonVoisinage][0],
                                                               self.im[y + rayonVoisinage][x + rayonVoisinage][1],
                                                               self.im[y + rayonVoisinage][x + rayonVoisinage][2])
                                n = n + 1
                    rayonVoisinage -= 1
                    voisinageParcourue = rayonVoisinage == 0
                # pixel central
                somme = somme + self.Intensite(self.im[y][x][0], self.im[y][x][1], self.im[y][x][2])

                n = n + 1
                imIntensiteMoy = somme / n
                intensite = int(
                    abs(self.Intensite(self.im[y][x][0], self.im[y][x][1], self.im[y][x][2]) - imIntensiteMoy))
                intensite = intensite ** 2
                self.imIntensite[y][x] = intensite
        print("thread: ", self.i, " termine")
        rep = [0, 0]
        rep[0] = self.imIntensite
        rep[1] = self.i
        self.queue.put(rep)

    def Intensite(self, r, g, b):
        return int((r + g + b) / 3)
