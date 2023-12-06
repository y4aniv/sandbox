def division_euclidienne(a, b):
    """
    Effectue la division euclidienne de a par b
    :entrée a: int, b: int
    :sortie: tuple(int, int)
    """
    assert type(a) == int and type(b) == int
    assert a >= 0 and b > 0

    return (a // b, a % b)

assert division_euclidienne(20, 3) == (6, 2)
assert type(division_euclidienne(20, 3)) == tuple


def parseNote(notes):
    """
    Retourne un tuple de notes sans les "abs"
    :entrée notes: tuple()
    :sortie: tuple(int)
    """
    assert type(notes) == tuple

    N = ()
    for note in notes:
        if note != "abs":
            N += (int(note),)
    return N

assert parseNote((12, 14, 8, "abs", 15, 14, "abs")) == (12, 14, 8, 15, 14)
assert type(parseNote((12, 14, 8, "abs", 15, 14, "abs"))) == tuple


def nbValeurs(l):
    """
    Retourne le nombre de valeurs dans le tuple sans "abs"
    :entrée l: tuple()
    :sortie: int
    """
    assert type(l) == tuple
    return len(parseNote(l))

assert nbValeurs((12, 14, 8, 15, 14)) == 5
assert nbValeurs((12, 14, 8, "abs", 15, 14, "abs")) == 5

def moyenne(l):
    """
    Retourne la moyenne des valeurs dans le tuple
    :entrée l: tuple()
    :sortie: float
    """

    assert type(l) == tuple
    assert nbValeurs(l) > 0

    l = parseNote(l)

    somme = 0
    for note in l:
        somme += note
    return somme / nbValeurs(l)

assert moyenne((12, 14, 8, 15, 14)) == 12.6
assert moyenne((12, 14, 8, "abs", 15, 14, "abs")) == 12.6

def infoNote(notes):
    """
    Retourne un tuple avec le nombre de notes et la moyenne
    :entrée notes: tuple()
    :sortie: tuple(int, float)
    """
    return(nbValeurs(notes), moyenne(notes))

assert infoNote((12, 14, 8, 15, 14)) == (5, 12.6)
assert infoNote((12, 14, 8, "abs", 15, 14, "abs")) == (5, 12.6)

def userIsMajor(user):
    """
    Retourne True si l'utilisateur est majeur, False sinon
    :entrée user: tuple(str, str, int, bool)
    :sortie: bool
    """
    assert type(user) == tuple
    assert type(user[2]) == int

    if user[2] >= 18:
        return True
    else:
        return False

def setUserMarried(user):
    """
    Affecte True à la dernière valeur du tuple pour indiquer que l'utilisateur est marié
    :entrée user: tuple(str, str, int, bool)
    :sortie: bool
    """
    assert type(user) == tuple
    assert type(user[3]) == bool

    user = list(user)
    user[3] = True

    return tuple(user)
    

assert userIsMajor(("yaniv", "douieb", 15, False)) == False
assert userIsMajor(("alexander", "douieb", 30, True)) == True

assert setUserMarried(("yaniv", "douieb", 15, False)) == ("yaniv", "douieb", 15, True)
assert setUserMarried(("alexander", "douieb", 30, True)) == ("alexander", "douieb", 30, True)