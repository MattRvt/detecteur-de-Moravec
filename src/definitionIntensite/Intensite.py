import time
from concurrent.futures import thread
from threading import Thread, RLock

verrou = RLock()


class Partie(Thread):
    # """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, minY, maxY, im, h, w):
        Thread.__init__(self)
        self.minY = minY
        self.maxY = maxY
        self.im = im
        self.h = h
        self.w = w
        self.imIntensite = [[0 for j in range(w)] for i in range(h)]

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        for y in range(self.minY,self.maxY):
            for x in range(self.w):
                rayonVoisinageStatic = 1
                rayonVoisinage = rayonVoisinageStatic
                voisinageParcourue = False
                intensitePixeles = 0
                p = self.im[y][x]
                somme = 0
                while not voisinageParcourue:
                    n = 0
                    # si on atteint le pas bord en haut de l'immage
                    if (y - rayonVoisinage >= 0):
                        # tout la rangee du haut
                        somme = somme + self.Intensite(self.im[y - rayonVoisinage][x][0],
                                                       self.im[y - rayonVoisinage][x][1],
                                                       self.im[y - rayonVoisinage][x][2])
                        n = n + 1
                    if (x - rayonVoisinage >= 0):
                        # haut gauche
                        somme = somme + self.Intensite(self.im[y - rayonVoisinage][x - rayonVoisinage][0],
                                                       self.im[y - rayonVoisinage][x - rayonVoisinage][1],
                                                       self.im[y - rayonVoisinage][x - rayonVoisinage][2])
                        n = n + 1
                        # haut droit
                    if (x + rayonVoisinage < self.w):
                        somme = somme + self.Intensite(self.im[y - rayonVoisinage][x + rayonVoisinage][0],
                                                       self.im[y - rayonVoisinage][x + rayonVoisinage][1],
                                                       self.im[y - rayonVoisinage][x + rayonVoisinage][2])
                        n = n + 1
                    #   si on atteint pas la limite gauche de l'image
                    if (x - rayonVoisinage >= 0):
                        # tout la rangee d'en bas
                        somme = somme + self.Intensite(self.im[y][x - rayonVoisinage][0],
                                                       self.im[y][x - rayonVoisinage][1],
                                                       self.im[y][x - rayonVoisinage][2])
                        n = n + 1
                    # bas gauche
                    if (y - rayonVoisinage >= 0):
                        somme = somme + self.Intensite(self.im[y - rayonVoisinage][x - rayonVoisinage][0],
                                                       self.im[y - rayonVoisinage][x - rayonVoisinage][1],
                                                       self.im[y - rayonVoisinage][x - rayonVoisinage][2])
                        n = n + 1
                        # bas droit
                    if (y + rayonVoisinage < self.h):
                        somme = somme + self.Intensite(self.im[y + rayonVoisinage][x - rayonVoisinage][0],
                                                       self.im[y + rayonVoisinage][x - rayonVoisinage][1],
                                                       self.im[y + rayonVoisinage][x - rayonVoisinage][2])
                        n = n + 1
                    rayonVoisinage -= 1
                    voisinageParcourue = rayonVoisinage == 0
                # pixel central
                somme = somme + self.Intensite(self.im[y][x][0], self.im[y][x][1], self.im[y][x][2])

                n = n + 1
                imIntensiteMoy = somme / n
                intensite = int(
                    abs(self.Intensite(self.im[y][x][0], self.im[y][x][1], self.im[y][x][2]) - imIntensiteMoy))
                intensite = intensite / (6 * rayonVoisinageStatic)
                self.imIntensite[y][x] = intensite

    def Intensite(self, r, g, b):
        return r * 1 + g * 3 + b * 2
