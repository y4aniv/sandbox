def ajout_dico(cle, valeur, dico):
    """
    Cette fonction permet de rajouter une clé et une valeur dans un dictionnaire si la clé n'existe pas

    entrées: cle (str), valeur (str), dico (dictionnaire)
    sortie: dictionnaire
    """
    if cle not in dico:
        dico[cle] = valeur
        return dico
    
def fustion_dico(dico1, dico2):
    """
    Cette fonction permet de fusionner deux dictionnaires en utilisant la fonction ajout_dico

    entrées: dico1 (dictionnaire), dico2 (dictionnaire)
    sortie: dictionnaire
    """

    for cle, valeur in dico2.items():
        ajout_dico(cle, valeur, dico1)
    dico2.clear()
    return dico1

fr_ang = {"chanson": "song", "glace": "ice", "feu": "fire" }
assert ajout_dico("livre", "book", fr_ang) == {"chanson": "song", "glace": "ice", "feu": "fire", "livre": "book"}
assert ajout_dico("chanson", "song", fr_ang) == None
assert ajout_dico("livre", "book", fr_ang) == None

dico1 = {"France": "Paris", "Allemagne": "Berlin", "Italie": "Rome"}
dico2 = {"Espagne": "Madrid", "Italie": "Rome", "France": "Paris"}
assert fustion_dico(dico1, dico2) == {"France": "Paris", "Allemagne": "Berlin", "Italie": "Rome", "Espagne": "Madrid"}