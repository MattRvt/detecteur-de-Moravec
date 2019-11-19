import imageio
import numpy

def Intensite(r, g, b):
   return (r**3)+ (g**2) + b

w=400
h=352
im = imageio.imread('chargementImage/arbre.jpg', format = 'jpg')
imIntensiteMoy = [[0 for j in range(w)] for i in range(h)]
imIntensite = [[0 for j in range(w)] for i in range(h)]
for y in range(h):
    for x in range(w):
         #print("-----")
         #print("x= "+str(x))
         #print("y= "+str(y))
         #print("-----")
         n=0
         somme=0
         p = im[y][x]
         if(y-1>=0):
            somme = somme + Intensite(im[y-1][x][0], im[y-1][x][1], im[y-1][x][2])
            n = n+1
            if(x-1>=0):
                somme = somme + Intensite(im[y-1][x-1][0], im[y-1][x-1][1], im[y-1][x-1][2]) 
                n = n+1
            if(x+1<w):
                somme = somme + Intensite(im[y-1][x+1][0], im[y-1][x+1][1], im[y-1][x+1][2])
                n = n+1
         if(x-1>=0):
            somme = somme + Intensite(im[y][x-1][0], im[y][x-1][1], im[y][x-1][2])
            n = n+1
            if(y-1>=0):
                somme = somme + Intensite(im[y-1][x-1][0], im[y-1][x-1][1], im[y-1][x-1][2]) 
                n = n+1
            if(y+1<h):
                somme = somme + Intensite(im[y+1][x-1][0], im[y+1][x-1][1], im[y+1][x-1][2])
                n = n+1
         somme = somme+Intensite(im[y][x][0], im[y][x][1], im[y][x][2])
         n = n+1
         imIntensiteMoy=somme/n
         imIntensite[y][x]= int(abs(Intensite(im[y][x][0], im[y][x][1], im[y][x][2]) - imIntensiteMoy)/65281)
         im[y][x][0] = imIntensite[y][x]
         im[y][x][1] = imIntensite[y][x]
         im[y][x][2] = imIntensite[y][x]
imageio.imsave('chargementImage/16t.jpg',im, format = 'jpg')

