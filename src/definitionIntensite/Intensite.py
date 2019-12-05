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
        for y in range(self.minY, self.maxY):
            for x in range(self.w):

                # pour chaque pixel
                rayonVoisinageStatic = 10
                p = self.im[y][x]
                intensiteP = self.Intensite(p[0], p[1], p[2])
                somme = 0
                n = 0
                for rayonVoisinage in range(0, rayonVoisinageStatic + 1):

                    rayonVoisinage = rayonVoisinage
                    # si on atteint le pas bord en haut de l'immage
                    if (y - rayonVoisinage >= 0):
                        # px du haut
                        Iuv = self.Intensite(self.im[y - rayonVoisinage][x][0],
                                             self.im[y - rayonVoisinage][x][1],
                                             self.im[y - rayonVoisinage][x][2])
                        diffIntensite = (intensiteP - Iuv) ** 2
                        somme = somme + (diffIntensite / (rayonVoisinage + 1))
                        n = n + 1

                        # px haut gauche
                        if (x - rayonVoisinageStatic >= 0):
                            for xTemp in range(x - rayonVoisinageStatic, x + 1):
                                Iuv = self.Intensite(self.im[y - rayonVoisinage][xTemp][0],
                                                     self.im[y - rayonVoisinage][xTemp][1],
                                                     self.im[y - rayonVoisinage][xTemp][2])
                                diffIntensite = (intensiteP - Iuv) ** 2
                                somme = somme + (diffIntensite / (rayonVoisinage + 1))
                                n = n + 1

                        # px haut droit
                        if (x + rayonVoisinageStatic < self.w):
                            for xTemp in range(x + 1, x + rayonVoisinageStatic + 1):
                                Iuv = self.Intensite(self.im[y - rayonVoisinage][xTemp][0],
                                                     self.im[y - rayonVoisinage][xTemp][1],
                                                     self.im[y - rayonVoisinage][xTemp][2])
                                diffIntensite = (intensiteP - Iuv) ** 2
                                somme = somme + (diffIntensite / (rayonVoisinage + 1))
                                n = n + 1

                        n = n + 1
                    #   si on atteint pas la limite bas de l'image
                    if (y + rayonVoisinage < self.h):
                        # px du bas
                        Iuv = self.Intensite(self.im[y + rayonVoisinage][x][0],
                                             self.im[y + rayonVoisinage][x][1],
                                             self.im[y + rayonVoisinage][x][2])
                        diffIntensite = (intensiteP - Iuv) ** 2
                        somme = somme + (diffIntensite / (rayonVoisinage + 1))
                        n = n + 1

                        # px haut gauche
                        if (x - rayonVoisinage >= 0):
                            for xTemp in range(x - rayonVoisinage, x + 1):
                                Iuv = self.Intensite(self.im[y + rayonVoisinage][xTemp][0],
                                                     self.im[y + rayonVoisinage][xTemp][1],
                                                     self.im[y + rayonVoisinage][xTemp][2])
                                diffIntensite = (intensiteP - Iuv) ** 2
                                somme = somme + (diffIntensite / (rayonVoisinage + 1))
                                n = n + 1

                        # px bas droit
                        if (x + rayonVoisinageStatic < self.w):
                            for xTemp in range(x + 1, x + rayonVoisinageStatic + 1):
                                Iuv = self.Intensite(self.im[y + rayonVoisinage][xTemp][0],
                                                     self.im[y + rayonVoisinage][xTemp][1],
                                                     self.im[y + rayonVoisinage][xTemp][2])
                                diffIntensite = (intensiteP - Iuv) ** 2
                                somme = somme + (diffIntensite / (rayonVoisinage + 1))
                                n = n + 1

                    # pixel a gauche
                    if (x - rayonVoisinage >= 0):
                        # px du haut
                        Iuv = self.Intensite(self.im[y][x - rayonVoisinage][0],
                                             self.im[y][x - rayonVoisinage][1],
                                             self.im[y][x - rayonVoisinage][2])
                        diffIntensite = (intensiteP - Iuv) ** 2
                        somme = somme + (diffIntensite / (rayonVoisinage + 1))
                        n = n + 1
                        #   si on atteint pas la limite bas de l'image
                    if (x + rayonVoisinage < self.w):
                        # px du bas
                        Iuv = self.Intensite(self.im[y][x + rayonVoisinage][0],
                                             self.im[y][x + rayonVoisinage][1],
                                             self.im[y][x + rayonVoisinage][2])
                        diffIntensite = (intensiteP - Iuv) ** 2
                        somme = somme + (diffIntensite / (rayonVoisinage + 1))
                        n = n + 1

                imIntensiteMoy = somme / n
                self.imIntensite[y][x] = imIntensiteMoy

        print("thread: ", self.i, " termine")
        rep = [0, 0]
        rep[0] = self.imIntensite
        rep[1] = self.i
        self.queue.put(rep)

    # renvoie une intensité entre 255 et 0
    def Intensite(self, r, g, b):
        return int((r + g + b) / 3)
