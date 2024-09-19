class Date:
    
    mois = [
        "janvier", 
        "février", 
        "mars",
        "avril",
        "mai", 
        "juin", 
        "juillet", 
        "août", 
        "septembre", 
        "octobre", 
        "novembre", 
        "décembre"
    ]
    nb_jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, jour: int, mois: int, annee: int):
        """
        Constructeur de la classe Date
        """
        if jour > 0 and jour <= Date.nb_jours[mois - 1] and mois > 0 and mois <= 12:
            self.jour = jour
            self.mois = mois
            self.annee = annee
        else:
            raise ValueError("La date n'est pas valide")
        
    def __str__(self) -> str:
        """
        Méthode spéciale qui renvoie une représentation de l'objet sous forme de chaîne de caractères
        """

        return f"{self.jour} {Date.mois[self.mois - 1]} {self.annee}"
    
    def __lt__(self, other) -> bool:
        """
        Méthode spéciale qui compare deux dates 
        """
        if self.annee < other.annee:
            return True
        elif self.annee == other.annee:
            if self.mois < other.mois:
                return True
            elif self.mois == other.mois:
                if self.jour < other.jour:
                    return True
        return False
    
    def __eq__(self, other) -> bool:
        """
        Méthode spéciale qui vérifie l'égalité de deux dates
        """
        if self.annee == other.annee and self.mois == other.mois and self.jour == other.jour:
            return True
    
    def lendemain(self) -> "Date":
        """
        Méthode qui renvoie la date du lendemain
        """
        if self.jour < Date.nb_jours[self.mois - 1]:
            return Date(self.jour + 1, self.mois, self.annee)
        elif self.mois < 12:
            return Date(1, self.mois + 1, self.annee)
        else:
            return Date(1, 1, self.annee + 1)


date1 = Date(20, 1, 2012)
date2 = Date(28, 2, 2022)

assert str(date1) == "20 janvier 2012"
assert date1 < date2
assert date1.lendemain() == Date(21, 1, 2012)
assert date2.lendemain() == Date(1, 3, 2022)
assert Date(31, 12, 2022).lendemain() == Date(1, 1, 2023)