def compte_base(sequence):
    """
    Cette fonction permet de savoir combien de fois chaque base est présente dans une séquence ADN

    entrée: sequence (str)
    sortie: dictionnaire
    """

    dico = {}
    valid_bases = "ATGC"
    for base in sequence:
        if base in valid_bases:
            if base in dico:
                dico[base] += 1
            else:
                dico[base] = 1
    return dico

fichierADN = open("fichierADN.txt", "r").read()

assert compte_base("ACCTAGCCCAG") ==  {'A': 3, 'T': 1, 'C': 5, 'G':2}
assert compte_base("HJGATGCTGUBACGATCMGA") == {'G': 5, 'A': 4, 'T': 3, 'C': 3}
assert compte_base(fichierADN) == {'A': 11, 'G': 12, 'T': 8, 'C': 8}
assert compte_base("KLODJDJNZ") == {}