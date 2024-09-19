class JoueurFoot:
    def __init__(self, nom: str, age: int, poste: str, prix: int, valide: bool = True):
        """
        Constructeur de la classe JoueurFoot
        """
        self.nom = nom
        self.age = age
        self.poste = poste
        self.prix = prix
        self.valide = valide

    def blessure(self):
        """
        Méthode mutatrice qui permet d'indiquer qu'un joueur est invalide
        """
        self.valide = False

    def soigne(self):
        """
        Méthode mutatrice qui permet d'indiquer qu'un joueur est valide
        """
        self.valide = True

class ClubFoot:
    def __init__(self, nom: str, ville: str, budget: int, joueurs: list = []):
        """
        Constructeur de la classe ClubFoot
        """
        self.nom = nom
        self.ville = ville
        self.budget = budget
        self.joueurs = joueurs

    def equipe(self) -> list:
        """
        Méthode qui renvoie la liste des nom des joueurs de l'équipe
        """
        return [joueur.nom for joueur in self.joueurs]
    
    def ajout_gratuit(self, joueur: JoueurFoot):
        """
        Méthode qui permet d'ajouter un joueur gratuitement dans l'équipe
        """
        self.joueurs.append(joueur)

    def peut_jouer(self) -> bool:
        """
        Méthode qui vérifie si le club à les moyens de jouer
        """
        budget_ok = self.budget >= 0
        nb_joueurs_ok = len([joueur for joueur in self.joueurs if joueur.valide]) >= 11
        nb_gardien_ok = len([joueur for joueur in self.joueurs if joueur.valide and joueur.poste == "Gardien"]) >= 1

        return nb_joueurs_ok and nb_joueurs_ok and nb_gardien_ok and budget_ok
        
    def transfert(self, joueur: JoueurFoot, club) -> str:
        """
        Méthode qui permet de transférer un joueur d'un club à un autre
        """

        if type(club) == ClubFoot:
            if joueur in club.joueurs:
                if self.budget >= joueur.prix:
                    self.joueurs.append(joueur)
                    club.joueurs.remove(joueur)
                    self.budget -= joueur.prix
                    club.budget += joueur.prix
                    return f"{joueur.nom} a été transféré de {club.nom} à {self.nom} pour un montant de {joueur.prix}€"
                else:
                    return f"{self.nom} n'a pas les moyens de transférer {joueur.nom}"
            else:
                return f"{joueur.nom} n'est pas dans l'équipe de {club.nom}"
        else:
            return "Le club n'est pas valide"

hugoLloris = JoueurFoot("Hugo Lloris", 37, "Gardien", 1200000)
lucasHernandez = JoueurFoot("Lucas Hernandez", 28, "Défenseur", 40000000)
ngoloKante = JoueurFoot("N'Golo Kanté", 33, "Milieu", 9000000)
kylianMbappe = JoueurFoot("Kylian Mbappé", 25, "Attaquant", 244000000)
theoHernandez = JoueurFoot("Theo Hernandez", 26, "Défenseur", 35000000)
raphaelVarane = JoueurFoot("Raphael Varane", 30, "Défenseur", 60000000)
aurelienTchouameni = JoueurFoot("Aurelien Tchouameni", 23, "Milieu", 80000000)
antoineGriezmann = JoueurFoot("Antoine Griezmann", 32, "Attaquant", 60000000)
dayotUpamecano = JoueurFoot("Dayot Upamecano", 25, "Défenseur", 50000000)
adrienRabiot = JoueurFoot("Adrien Rabiot", 28, "Gardien", 35000000)  # C'est pas un gardien mais pour les besoins du test...
olivierGiroud = JoueurFoot("Olivier Giroud", 37, "Attaquant", 15000000)
mikelOyarzabal = JoueurFoot("Mikel Oyarzabal", 26, "Attaquant", 55000000)

parisSaintGermain = ClubFoot("Paris Saint-Germain", "Paris", 700000000, [])
realMadrid = ClubFoot("Real Madrid", "Madrid", 270000000, [
    lucasHernandez, 
    ngoloKante,
    kylianMbappe, 
    theoHernandez, 
    raphaelVarane, 
    aurelienTchouameni, 
    antoineGriezmann, 
    dayotUpamecano, 
    adrienRabiot, 
    olivierGiroud, 
    mikelOyarzabal
])

assert parisSaintGermain.equipe() == []
parisSaintGermain.ajout_gratuit(hugoLloris)
assert parisSaintGermain.equipe() == ["Hugo Lloris"]

assert parisSaintGermain.peut_jouer() == False
assert realMadrid.peut_jouer() == True

assert parisSaintGermain.equipe() == ["Hugo Lloris"]
assert parisSaintGermain.budget == 700000000
parisSaintGermain.transfert(theoHernandez, realMadrid)
assert parisSaintGermain.equipe() == ["Hugo Lloris", "Theo Hernandez"]
assert parisSaintGermain.budget == 665000000
assert realMadrid.budget == 305000000