import imageio

def Intensite(r, g, b):
   return (r**3)+ (g**2) + b


im = imageio.imread('chargementImage/16.png')
imIntensite = [[0 for j in range(16)] for i in range(16)]
for ligne in range(16):
    for pixel in range(16):
        p = im[ligne][pixel]
        imIntensite[ligne][pixel]=Intensite(p[0], p[1], p[2])
print(imIntensite)
