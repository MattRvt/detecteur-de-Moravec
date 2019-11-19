#import numpy

def Intensite(r, g, b):
   return (r**3)+ (g**2) + b

##def Fenetre(image, centre, rayon):
##   ligneTotal = len(image)
##   colonneTotal =len(image[0])
##   fenetre = numpy.ones((rayon+2, rayon+2))
##   return fenetre
##   
##
##w = 5
##h = 2
##
##image = [[[255,255,255],[0,0,0],[125,30,230],[230,230,230],[128,80,68]],
##          [[255,18,255],[96,0,8],[120,30,230],[196,20,158],[68,80,68]]]
##print(Fenetre(image, 0, 5))
####for y in range(h):
####   for x in range(w):
####      if(x <w-1):
####         pixel = image[y][x]
####         pixelDroite = image[y][x+1]
####         r=pixel[0]
####         g=pixel[1]
####         b=pixel[2]
####         r2=pixelDroite[0]
####         g2=pixelDroite[1]
####         b2=pixelDroite[2]
####         print((Intensite(r, g, b)-Intensite(r2, g2, b2))**2)
####      
##   
