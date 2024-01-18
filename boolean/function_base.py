def meme_longeur(liste1, liste2):
    """
    Permet de savoir si deux listes ont la même longeur

    entrée: liste1 <list>
    entrée: liste2 <list>

    sortie: <bool>
    """

    assert type(liste1) == list
    assert type(liste2) == list

    return len(liste1) == len(liste2)

def compte(element, liste):
    """
    Renvoie le nombre d'élément dans la liste

    entrée: element <str>
    entrée: liste <list>

    sortie: <int>
    """

    assert type(element) == str
    assert type(liste) == list

    count = 0
    for e in liste:
        if e == element:
            count += 1

    return count

def begaye(liste):
    """
    Renvoie une nouvelle liste avec chaque élément écris deux fois d'affiler

    entrée: liste <list>

    sortie : <list>
    """

    assert type(liste) == list

    return [element for element in liste for _ in range(2)]

def maxListe(liste):
    """
    Renvoie le maximume d'une liste composé uniquement d'entier

    entrée: liste <list>

    sortie: maximum <int>
    """

    assert type(liste) == list

    maximum = None

    for e in liste:
        assert type(e) == int
        if maximum == None or e > maximum:
            maximum = e

    return maximum

assert meme_longeur([1, 2, 3], [1, 2, 3]) == True
assert meme_longeur([1, 2, 3], [1, 2]) == False

assert compte("a", ["a", "b", "c", "a", "a"]) == 3
assert compte("a", ["b", "c", "d"]) == 0

assert begaye(["a", "b", "c"]) == ["a", "a", "b", "b", "c", "c"]
assert begaye(["a", "b", "c", "d"]) == ["a", "a", "b", "b", "c", "c", "d", "d"]

assert maxListe([1, 2, 3, 4, 5]) == 5
assert maxListe([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9