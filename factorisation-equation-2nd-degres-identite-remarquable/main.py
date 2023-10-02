

import math

# Fonction pour calculer le PGCD de deux nombres en utilisant l'algorithme d'Euclide
def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Fonction pour trouver le facteur commun de trois nombres
def facteur_commun_de_trois_nombres(num1, num2, num3):
    # Calculer le PGCD des deux premiers nombres
    pgcd1 = pgcd(num1, num2)
    
    # Calculer le PGCD du résultat précédent et du troisième nombre
    pgcd_final = pgcd(pgcd1, num3)
    
    return pgcd_final

# Exemple d'utilisation
method = int(input("Méthode : "))


if(method == 1):
    nombre1 = int(input("A : "))
    nombre2 = int(input("B : "))
    nombre3 = int(input("C : "))
    resultat = facteur_commun_de_trois_nombres(nombre1, nombre2, nombre3)

    DELTA = nombre2**2 - 4*nombre1*nombre3

    if(DELTA != 0):
        print("ATTENTION : DELTA != 0")


    print(f"Facteur commun : {resultat}")
    print(f"\n{resultat}({nombre1/resultat}x² + {nombre2/resultat}x + {nombre3/resultat})")

    # si nombre2/resultat est négatif
    if nombre2/resultat < 0:
        print(f"{resultat}({math.sqrt(nombre1/resultat)}x - {math.sqrt(nombre3/resultat)})²")
    else:
        print(f"{resultat}({math.sqrt(nombre1/resultat)}x + {math.sqrt(nombre3/resultat)})²")

elif(method == 2):
    nombre1 = int(input("A : "))
    nombre2 = int(input("B : "))
    nombre3 = int(input("C : "))
    print(f"(√{nombre1}x + √{nombre3})(√{nombre1}x - √{nombre3})")

    DELTA = nombre2**2 - 4*nombre1*nombre3
    print(f"DELTA = {DELTA}")
    if(DELTA > 0):
        x1 = (-nombre2 + math.sqrt(DELTA)) / (2*nombre1)
        x2 = (-nombre2 - math.sqrt(DELTA)) / (2*nombre1)

        print(f"\nDELTA = {DELTA}")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

        print(f"\n{nombre1}(x - {x1})(x - {x2})")