# Description: Solve equation with fonctions
# Author: Yaniv Douieb (y4aniv)
# Language: Python 3.10.8

A = input("A = ")
B = input("B = ")
C = input("C = ")

def linear(a, b):
    """
    entree : a, b (int)
    sortie : equa, result (str)
    """
    x = -b / a
    
    equa = f"Il s'agit d'une équation du premier degré : {a}x + {b} = 0"
    result = f"La solution est : x = {x}"

    return equa, result

def quadratic(a, b, c):
    """
    entree : a, b, c (int)
    sortie : equa, result (str)
    """
    DELTA = b**2 - 4*a*c
    
    if(DELTA < 0):
        equa = f"Il s'agit d'une équation du second degré : {a}x² + {b}x + {c} = 0"
        result = "Cette équation n'a pas de solution dans R"
    elif(DELTA == 0):
        x = -b / (2*a)

        equa = f"Il s'agit d'une équation du second degré : {a}x² + {b}x + {c} = 0"
        result = f"La solution est : x = {x}"
    else:
        x1 = (-b - DELTA**0.5) / (2*a)
        x2 = (-b + DELTA**0.5) / (2*a)

        equa = f"Il s'agit d'une équation du second degré : {a}x² + {b}x + {c} = 0"
        result = f"Les solutions sont : x1 = {x1} et x2 = {x2}"

    return equa, result

def constant(a):
    """
    entree : a (int)
    sortie : equa, result (str)
    """
    if(a == 0):
        equa = "Il s'agit d'une équation du type 0 = 0"
        result = "Cette équation a une infinité de solutions"
    else:
        equa = "Il s'agit d'une équation du type 0 = a (a ≠ 0)"
        result = "Cette équation n'a pas de solution dans R"

    return equa, result

def resolve(a, b, c):
    """
    entree : a, b, c (int)
    sortie : x (int) ou x1, x2 (tuple)
    """
    if(a == 0):
        return linear(b, c)

    if(a != 0):
        return quadratic(a, b, c)
    
    if(a == 0 and b == 0):
        return constant(c)
    
    if(a == 0 and b == 0 and c == 0):
        return constant(c)

print(resolve(int(A), int(B), int(C)))