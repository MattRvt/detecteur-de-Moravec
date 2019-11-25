import imageio
import numpy


def Intensite(r, g, b):
    return r * 1 + g * 3 + b * 2


# def MoyenneIntensite(image, rayon, hauteur, largeur, posX, posY, somme, nbCase):


im = imageio.imread('chargementImage/arbre.jpg', format='jpg')
info = im.shape
h = info[0]
w = info[1]
imIntensiteMoy = [[0 for j in range(w)] for i in range(h)]
imIntensite = [[0 for j in range(w)] for i in range(h)]

for y in range(h):
    for x in range(w):
        rayonVoisinageStatic = 2
        rayonVoisinage = rayonVoisinageStatic
        voisinageParcourue = False
        intensitePixeles = 0
        p = im[y][x]
        somme = 0
        while not voisinageParcourue:
            n = 0
            # si on atteint le pas bord en haut de l'immage
            if (y - rayonVoisinage >= 0):
                # tout la rangee du haut
                somme = somme + Intensite(im[y - rayonVoisinage][x][0],
                                          im[y - rayonVoisinage][x][1],
                                          im[y - rayonVoisinage][x][2])
                n = n + 1
            if (x - rayonVoisinage >= 0):
                # haut gauche
                somme = somme + Intensite(im[y - rayonVoisinage][x - rayonVoisinage][0],
                                          im[y - rayonVoisinage][x - rayonVoisinage][1],
                                          im[y - rayonVoisinage][x - rayonVoisinage][2])
                n = n + 1
                # haut droit
            if (x + rayonVoisinage < w):
                somme = somme + Intensite(im[y - rayonVoisinage][x + rayonVoisinage][0],
                                          im[y - rayonVoisinage][x + rayonVoisinage][1],
                                          im[y - rayonVoisinage][x + rayonVoisinage][2])
                n = n + 1
            #   si on atteint pas la limite gauche de l'image
            if (x - rayonVoisinage >= 0):
                # tout la rangee d'en bas
                somme = somme + Intensite(im[y][x - rayonVoisinage][0],
                                          im[y][x - rayonVoisinage][1],
                                          im[y][x - rayonVoisinage][2])
                n = n + 1
            # bas gauche
            if (y - rayonVoisinage >= 0):
                somme = somme + Intensite(im[y - rayonVoisinage][x - rayonVoisinage][0],
                                          im[y - rayonVoisinage][x - rayonVoisinage][1],
                                          im[y - rayonVoisinage][x - rayonVoisinage][2])
                n = n + 1
                # bas droit
            if (y + rayonVoisinage < h):
                somme = somme + Intensite(im[y + rayonVoisinage][x - rayonVoisinage][0],
                                          im[y + rayonVoisinage][x - rayonVoisinage][1],
                                          im[y + rayonVoisinage][x - rayonVoisinage][2])
                n = n + 1
            rayonVoisinage -= 1
            voisinageParcourue = rayonVoisinage == 0
        # pixel central
        somme = somme + Intensite(im[y][x][0], im[y][x][1], im[y][x][2])
        
        n = n + 1
        imIntensiteMoy = somme / n
        intensite = int(abs(Intensite(im[y][x][0], im[y][x][1], im[y][x][2]) - imIntensiteMoy))
        intensite = intensite / (6*rayonVoisinageStatic)
        imIntensite[y][x] = intensite

# definit le code RGB de chaque pixel
for y in range(h):
    for x in range(w):
        if (imIntensite[y][x] > 40):
            im[y][x][0] = 0 #imIntensite[y][x]*2
            im[y][x][1] = 255
            im[y][x][2] = 0
        else:
            im[y][x][0] = 0
            im[y][x][1] = 0
            im[y][x][2] = 0

imageio.imsave('chargementImage/arbre.png', im, format='png')
