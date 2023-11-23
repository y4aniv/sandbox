def Split(string, sep):
    
    """Fonction qui sépare une chaîne de caractères en fonction d'un séparateur sans utiliser
    Entrée: string (str), sep (str)
    Sortie: liste (list)"""

    liste = []
    mot = ""
    for i in string:
        if i == sep:
            liste.append(mot)
            mot = ""
        else:
            mot += i
    liste.append(mot)
    return liste

def SVC_to_CSV(SVC):

    """Transforme une phrase de la forme Sujet Verbe Complément en Complément Sujet Verbe
    Exemple: Je suis beau -> Beau je suis
    Entrée: SVC (str)
    Sortie: CSV (str)"""

    SVC = Split(SVC, " ")
    S = SVC[0]
    V = SVC[1]
    C = SVC[2].capitalize()
    CSV = f'{C} {S} {V}'

    return CSV


# SVC = input("Phrase (Sujet Verbe Complément) >>> ")
# print(f"Phrase (Complément Sujet Verbe) >>> {SVC_to_CSV(SVC)}")


assert SVC_to_CSV("Je suis beau") == "Beau Je suis"
assert SVC_to_CSV("Tu manges demain") == "Demain Tu manges"
assert SVC_to_CSV("Robert est sympa") == "Sympa Robert est"