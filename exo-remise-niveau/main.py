def somme(L):
    """
    Calcule la somme des éléments d'une liste

    Args:
    L (list): liste d'entiers

    Returns:
    int: somme des éléments de la liste
    """
    assert type(L) == list, "L doit être une liste"
    assert all(type(x) == int for x in L), "Les éléments de L doivent être des entiers"

    somme = 0

    for x in L:
        somme += x

    return somme

def maxi(L):
    """
    Calcule le maximum des éléments d'une liste

    Args:
    L (list): liste d'entiers

    Returns:
    int: maximum des éléments de la liste
    """
    assert type(L) == list, "L doit être une liste"
    assert all(type(x) == int for x in L), "Les éléments de L doivent être des entiers"

    max = L[0]

    for x in L:
        if x > max:
            max = x

    return max

def mini(L):
    """
    Calcule le minimum des éléments d'une liste

    Args:
    L (list): liste d'entiers

    Returns:
    int: minimum des éléments de la liste
    """
    assert type(L) == list, "L doit être une liste"
    assert all(type(x) == int for x in L), "Les éléments de L doivent être des entiers"

    min = L[0]

    for x in L:
        if x < min:
            min = x

    return min

def puissance(x, n):
    """
    Calculer la puissance d'un nombre

    Args:
    x (int): nombre
    n (int): exposant

    Returns:
    int: x^n
    """
    assert type(x) == int, "x doit être un entier"
    assert type(n) == int, "n doit être un entier"
    assert n >= 0, "n doit être positif"

    p = 1

    for i in range(n):
        p *= x

    return p

def inverse(mot):
    """
    Inverser un mot

    Args:
    mot (str): mot

    Returns:
    str: mot inversé
    """
    assert type(mot) == str, "mot doit être une chaîne de caractères"

    return mot[::-1]

def tri_insertion(L):
    """
    Tri par insertion

    Args:
    L (list): liste d'entiers

    Returns:
    list: liste triée
    """
    assert type(L) == list, "L doit être une liste"
    assert all(type(x) == int for x in L), "Les éléments de L doivent être des entiers"

    n = len(L)
    for k in range(1, n):
        j = k
        while j > 0 and L[j-1] > L[j]:
            L[j-1], L[j] = L[j], L[j-1]
            j -= 1

    return L

assert somme([1, 2, 3, 4, 5]) == 15
assert maxi([1, 2, 3, 4, 5]) == 5
assert mini([1, 2, 3, 4, 5]) == 1
assert puissance(2, 3) == 8
assert inverse("hello") == "olleh"
assert tri_insertion([5, 3, 4, 1, 2]) == [1, 2, 3, 4, 5]