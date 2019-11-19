import imageio
import numpy

def Intensite(r, g, b):
   return (r**3)+ (g**2) + b

im = imageio.imread('chargementImage/16.png', format = 'png')
imIntensiteMoy = [[0 for j in range(16)] for i in range(16)]
imIntensite = [[0 for j in range(16)] for i in range(16)]
for y in range(16):
    for x in range(16):
        n=0
        somme=0
        p = im[y][x]
        if(y-1>=0):
            somme = somme + Intensite(im[y-1][x][0], im[y-1][x][1], im[y-1][x][2])
            n = n+1
            if(x-1>=0):
                somme = somme + Intensite(im[y-1][x-1][0], im[y-1][x-1][1], im[y-1][x-1][2]) 
                n = n+1
            if(x+1<16):
                somme = somme + Intensite(im[y-1][x+1][0], im[y-1][x+1][1], im[y-1][x+1][2])
                n = n+1
        if(x-1>=0):
            somme = somme + Intensite(im[y][x-1][0], im[y][x-1][1], im[y][x-1][2])
            n = n+1
            if(y-1>=0):
                somme = somme + Intensite(im[y-1][x-1][0], im[y-1][x-1][1], im[y-1][x-1][2]) 
                n = n+1
            if(y+1<16):
                somme = somme + Intensite(im[y+1][x-1][0], im[y+1][x-1][1], im[y+1][x-1][2])
                n = n+1
        somme = somme+Intensite(im[y][x][0], im[y][x][1], im[y][x][2])
        n = n+1
        imIntensiteMoy=somme/n
        imIntensite[y][x]= int(abs(Intensite(im[y][x][0], im[y][x][1], im[y][x][2]) - imIntensiteMoy)/65281)
print(imIntensite)
for y in range(16):
   for x in range(16):
      im[y][x][0] = imIntensite[y][x]
      im[y][x][1] = imIntensite[y][x]
      im[y][x][2] = imIntensite[y][x]
imageio.imsave('chargementImage/16t.png',im, format = 'png')

