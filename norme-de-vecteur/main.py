# Description : Find the norm and angle of a vector
# Author : Yaniv Douieb (y4aniv)
# Language : Python 3.10.8


# importation des modules ######################

import math


# definitions des fonctions ####################

def norme(x, y) :
    """ entrees : coordonnees x et y d'un vecteur (int ou float)
        sortie : renvoie la norme (float) arrondi a 2 decimales"""
    n = math.sqrt(x*x + y*y)    # sqrt est la racine carre
    return round(n, 2)          # pour arrondir a 2 decimales


def angle_hor(x, y) :
    """ entrees : coordonnees x et y d'un vecteur (int ou float)
        sortie : renvoie l'angle en degres avec l'axe horizontal, arrondi a 2 decimales"""
    if norme(x, y) == 0 :
        a = 0
    else :
        a = math.asin(y / norme(x, y))  # arcsinus donne un angle en radian

    a = math.degrees(a)     # convertit l'angle en degres
    a = round(a, 2)
    return a

def normeD(x, y, d) :
    """ entrees : coordonnees x et y d'un vecteur (int ou float)
        sortie : renvoie la norme (float) arrondi a d decimales"""
    n = math.sqrt(x*x + y*y)    # sqrt est la racine carre
    return round(n, d)          # pour arrondir a d decimales




# corps du programme ######################

vx = 0
vy = -10
print ("Vecteur de coordonnees (" + str(vx) + ", " + str(vy) + ") ")
print( "   Norme : " + str(norme(vx, vy)))
print ("   Angle avec l'horizontale : " + str(angle_hor(vx, vy)) + " degres.")
print()     # pour sauter une ligne

##x1 = 5
##y1 = 5
##print ("Vecteur de coordonnees (" + str(x1) + ", " + str(y1) + ") ")
##print( "   Norme : " + str(norme(x1, y1)))
##print ("   Angle avec l'horizontale : " + str(angle_hor(x1, y1)) qrkrrùrmfrkmffrl;fr;l;l;l;:ldfd,;*