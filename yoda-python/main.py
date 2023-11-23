def SVC_to_CSV(SVC):
    
    """Transforme une phrase de la forme Sujet Verbe Complément en Complément Sujet Verbe
    Exemple: "Je suis beau" -> "Beau Je suis"
    Entrée: SVC (str)
    Sortie: CSV (str)
    """

    s1 = SVC.index(" ")
    s2 = SVC[s1+1:].index(" ")+s1+1

    Sujet = SVC[0:s1]
    Verbe = SVC[s1+1:s2]
    Complement = SVC[s2+1:].capitalize()

    return f'{Complement} {Sujet} {Verbe}'

# SVC = input("Phrase (Sujet Verbe Complément) >>> ")
# print(f"Phrase (Complément Sujet Verbe) >>> {SVC_to_CSV(SVC)}")

assert SVC_to_CSV("Je suis beau") == "Beau Je suis"
assert SVC_to_CSV("Tu manges demain") == "Demain Tu manges"
assert SVC_to_CSV("Robert est sympa") == "Sympa Robert est"