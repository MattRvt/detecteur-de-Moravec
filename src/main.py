import psutil
import os
import imageio
from src.definitionIntensite.Intensite import Partie


def priority():
    """is called at every process start"""
    p = psutil.Process(os.getpid())
    # set to lowest priority, this is windows only, on Unix use ps.nice(19)
    p.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)


try:
    priority()
except:
    print("pour de meilleur performance installez psutil sur votre systeme.")
im = imageio.imread('chargementImage/arbre.png', format='png')
info = im.shape
h = info[0]
w = info[1]
imIntensiteMoy = [[0 for j in range(w)] for i in range(h)]

# creation des partie
partie1 = Partie(int(0 * (h / 4)), int(1 * (h / 4)), im, h, w)
partie2 = Partie(int(1 * (h / 4)), int(2 * (h / 4)), im, h, w)
partie3 = Partie(int(2 * (h / 4)), int(3 * (h / 4)), im, h, w)
partie4 = Partie(int(3 * (h / 4)), int(4 * (h / 4)), im, h, w)

# demarage des thread
partie1.start()
partie2.start()
partie3.start()
partie4.start()

# attent fin des thread  et concatenation des donnes
imIntensite = []
partie1.join()
imIntensite += partie1.imIntensite[int(0 * (h / 4)):int(1 * (h / 4))]
partie2.join()
imIntensite += partie2.imIntensite[int(1 * (h / 4)):int(2 * (h / 4))]
partie3.join()
imIntensite += partie3.imIntensite[int(2 * (h / 4)):int(3 * (h / 4))]
partie4.join()
imIntensite += partie4.imIntensite[int(3 * (h / 4)):int(4 * (h / 4))]

# definit le code RGB de chaque pixel
print("ecriture de l'image ")
for y in range(h):
    for x in range(w):
        contraste = 50
        if imIntensite[y][x] > 0:
            im[y][x][0] = (255 - imIntensite[y][x] * contraste)
            im[y][x][1] = (255 - imIntensite[y][x] * contraste)
            im[y][x][2] = (255 - imIntensite[y][x] * contraste)
        else:
            im[y][x][0] = 0
            im[y][x][1] = 0
            im[y][x][2] = 0

imageio.imsave('chargementImage/france.png', im, format='png')
