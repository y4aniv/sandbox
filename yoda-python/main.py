def SVC_to_CSV(SVC):
    
    """Transforme une phrase de la forme Sujet Verbe Complément en Complément Sujet Verbe
    Exemple: "Je suis beau" -> "Beau Je suis"
    Entrée: SVC (str)
    Sortie: CSV (str)
    """

    space1 = SVC.index(" ")
    space2 = SVC[space1+1:].index(" ") + space1 + 1

    sujet = SVC[0:space1]
    verbe = SVC[space1+1:space2]
    complement = SVC[space2+1:].capitalize()

    return f'{complement} {sujet} {verbe}'

# SVC = input("Phrase (Sujet Verbe Complément) >>> ")
# print(f"Phrase (Complément Sujet Verbe) >>> {SVC_to_CSV(SVC)}")

assert SVC_to_CSV("Je suis beau") == "Beau Je suis"
assert SVC_to_CSV("Tu manges demain") == "Demain Tu manges"
assert SVC_to_CSV("Robert est sympa") == "Sympa Robert est"