# Créé par ADAM, le 19/07/2023 en Python 3.7
import random

class Personnage:

    def __init__(self, nom, pv_max, force, vitesse = 10):
        """constructeur, ou initialiseur, il definit les attributs """
        self.nom = nom          # attribut nom : str
        self.pv_max = pv_max    # attribut pv_max : int
        self.pv = pv_max        # attribut pv : int
        self.vitesse = vitesse  # attribut vitesse : int
        self.__force = force      # attribut __force : int (privé)
        self.__nbPotions = 3    # attribut __nbPotions : int (privé)

    def vivant(self):
        """renvoie True si le personnage est vivant donc a plus de O points de vie"""
        return self.pv > 0

    def get_nom(self):
        """assesseur pour l'attribut nom"""
        return self.nom

    def get_pv(self):
        """assesseur pour l'attribut pv"""
        return self.pv

    def get_force(self):
        """assesseur pour l'attribut __force"""
        return self.__force

    def set_pv(self, points):
        """mutateur pour l'attibut pv"""
        if points > 0 and points <= self.pv_max:
            self.pv = points
        return self.pv
    
    def boit_potion(self):
        """methode qui permet de boire une potion"""
        if self.vivant():
            if self.__nbPotions > 0:
                self.__nbPotions -= 1
                self.pv *= 2
                if self.pv > self.pv_max:
                    self.pv = self.pv_max
        return self.pv
    
    def attaque(self, cible):
        if(random.randint(0, 1) == 0):
            cible.set_pv(cible.get_pv() - random.randint(1, self.__force))


    def __str__(self):
        """personnalisation de la méthode speciale d'affichage"""
        return "Nom: " + self.nom + " Points de vie: " + str(self.pv) + " Force: " + str(self.__force)


###### programme principal

# instanciation : creation d'objets
bilbo = Personnage("Bilbo Baggins", 20, 6)
gollum = Personnage("Gollum Smeagol", 10, 8)
gandalf = Personnage("Gandalf", 30, 10)
elrond = Personnage("Elrond", 25, 9, 20)

# recuperation d'une valeur d'attribut public (mauvaise façon mais ça marche)
print(bilbo.nom)

# modification d'une valeur d'attribut public (mauvaise façon mais ça marche)
bilbo.pv = 100
print(bilbo.pv)

# tentative de recuperation d'une valeur d'attribut privé (ça ne marche PAS car privé)
##print(gollum.__force)

# utilisation de la méthode vivant() sur l'objet bilbo
print(bilbo.vivant())

# recuperation d'une valeur d'attribut, public ou privé (BONNE façon !)
print(bilbo.get_nom())
print(gollum.get_force())

# modification d'une valeur d'attribut, public ou privé (BONNE façon !)
bilbo.set_pv(50)
print(bilbo.get_pv())

# test de l'affichage personnalisé
print(bilbo)

# récupération du nom de gandalf
print(gandalf.get_nom())

# utilisation de la méthode vivant() sur l'objet gandalf
gandalf.vivant()

gandalf.set_pv(5)
gandalf.boit_potion()
assert gandalf.get_pv() == 10

gollum.set_pv(6)
gollum.boit_potion()
assert gollum.get_pv() == 10
