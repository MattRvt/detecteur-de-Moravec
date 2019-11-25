import imageio
from src.definitionIntensite.Intensite import Partie

# def MoyenneIntensite(image, rayon, hauteur, largeur, posX, posY, somme, nbCase):


im = imageio.imread('chargementImage/mel.png', format='png')
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

# attent fin des thread
partie1.join()
partie2.join()
partie3.join()
partie4.join()

# concatenation des donnes
imIntensite =   partie1.imIntensite[int(0 * (h / 4)):int(1 * (h / 4))] \
              + partie2.imIntensite[int(1 * (h / 4)):int(2 * (h / 4))] \
              + partie3.imIntensite[int(2 * (h / 4)):int(3 * (h / 4))] \
              + partie4.imIntensite[int(3 * (h / 4)):int(4 * (h / 4))]

# definit le code RGB de chaque pixel
for y in range(h):
    for x in range(w):
        if (imIntensite[y][x] > 40):
            im[y][x][0] = 0  # imIntensite[y][x]*2
            im[y][x][1] = 255
            im[y][x][2] = 0
        else:
            im[y][x][0] = 0
            im[y][x][1] = 0
            im[y][x][2] = 0

imageio.imsave('chargementImage/arbre.png', im, format='png')
