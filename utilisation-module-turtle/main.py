# Description : Discover the turtle module
# Author : Yaniv Douieb (y4aniv)
# Language : Python 3.10.8

# importation des modules ###################

import turtle as tu         # le module 'turtle' est renomme 'tu' dans ce script


# definitions des fonctions ###################

def carre(taille, couleur):
    """entrees : taille en pixel (int) et couleur (str)
       sortie : dessine le carre correspondant avec le module turtle"""
    tu.color(couleur)
    c = 0
    while c < 4 :       # boucle conditionnelle, repetee TANT QUE c inferieur a 4
        tu.forward(taille)
        tu.right(90)
        c = c + 1

def triangle(taille, couleur, angle):
    """entrees : taille en pixel (int) et couleur (str)
       sortie : dessine le triangle correspondant avec le module turtle"""
    tu.right(angle)
    tu.color(couleur)
    c = 0
    while c < 3 :       # boucle conditionnelle, repetee TANT QUE c inferieur a 4
        tu.forward(taille)
        tu.left(120)
        c = c + 1


def etoile5(taille, couleur):
    """entrees : taille en pixel (int) et couleur (str)
       sortie : dessine l'etoile correspondant avec le module turtle"""
    tu.color(couleur)
    tu.begin_fill()
    c = 0
    while c < 5 :       # boucle conditionnelle, repetee TANT QUE c inferieur a 4
        tu.forward(taille)
        tu.right(144)
        c = c + 1
    tu.end_fill()

# corps du programme ######################

tu.speed(0)

carre(100, "red")
carre(50, "blue")
carre(25, "green")

triangle(100, "red", 60)
triangle(100, "blue", 60)
triangle(100, "green", 60)
triangle(100, "yellow", 60)
triangle(100, "purple", 60)
triangle(100, "orange", 60)

etoile5(100, "yellow")

tu.mainloop()
