# Description: Solve equation 2nd degres
# Author: Yaniv Douieb (y4aniv)
# Language: Python 3.10.8

import re

# Demandez à l'utilisateur d'entrer une équation du second degré
equation = input("Entrez une équation du second degré : ")

# Modèle de regex pour correspondre à une équation du second degré
pattern = r"^(-?\d*)([a-zA-Z])\^2 *([+-] *\d*)\2 *([+-] *\d+) *= *0$"

# Tentez de trouver une correspondance entre l'équation entrée et le modèle regex
match = re.match(pattern, equation)

# Vérifiez si l'équation se termine par "=0". Si non, ajoutez "=0" et refaites correspondre.
if equation[-2:] != "=0":
    equation += "=0"
    match = re.match(pattern, equation)

try:
    c = int(match.group(4))
except:
    # Si aucune valeur de 'c' n'est trouvée, modifiez l'équation pour avoir "+0" et refaites correspondre.
    equation = equation.replace("=0", "") + "+0" + "=0"
    match = re.match(pattern, equation)
    c = 0

try:
    a = int(match.group(1))
except:
    # Si aucune valeur de 'a' n'est trouvée, définissez 'a' sur 1.
    a = 1

try:
    b = int(match.group(3))
except:
    # Si aucune valeur de 'b' n'est trouvée, définissez 'b' sur 0.
    b = 0

if a == 0:
    result = f"L'équation {equation} n'est pas du second degré."
else:
    # Calcul du discriminant DELTA
    DELTA = b**2 - 4 * a * c

    if DELTA < 0:
        result = f"L'équation {equation} n'admet aucune solution."
    elif DELTA == 0:
        # Calcul de la solution unique si DELTA est égal à zéro
        x0 = round(-b / (2 * a), 3)
        result = f"L'équation {equation} admet une solution unique : S={{ {x0} }}"
    else:
        # Calcul des deux solutions si DELTA est positif
        x1 = round((-b + DELTA**0.5) / (2 * a), 3)
        x2 = round((-b - DELTA**0.5) / (2 * a), 3)
        result = f"L'équation {equation} admet deux solutions : S={{ {x1}, {x2} }}"

# Afficher le résultat
print(result)
