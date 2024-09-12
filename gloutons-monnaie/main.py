def rendu(somme_a_rendre):
    """
    Algorithme glouton pour rendre la monnaie

    Args:
    n (int): montant à rendre

    Returns:
    tuple: nombre de pièces de 5, 2 et 1 à rendre
    """
    assert somme_a_rendre > 0, "Le montant doit être non nul et positif"
    assert type(somme_a_rendre) == int, "Le montant doit être un entier"

    pieces = [5, 2, 1]
    rendu = ()

    for piece in pieces:
        rendu += (somme_a_rendre // piece,)
        somme_a_rendre %= piece
    
    return rendu

assert rendu(13) == (2, 1, 1)
assert rendu(64) == (12, 2, 0)
assert rendu(89) == (17, 2, 0)