# Description: Find the max of 4 numbers
# Author : Yaniv Douieb (y4aniv)
# Language : Python 3.10.8

# Définir la fonction max4 avec 4 paramètres (n1, n2, n3, n4)
def max4(n1, n2, n3, n4):
    # Définir les variables max1 et max2
    max1 = None
    max2 = None

    # Si n1 est plus grand que n2, max1 est égal à n1, sinon max1 est égal à n2
    if(n1 > n2):
        max1 = n1
    else:
        max1 = n2

    # Si n3 est plus grand que n4, max2 est égal à n3, sinon max2 est égal à n4
    if(n3 > n4):
        max2 = n3
    else:
        max2 = n4

    # Si max1 est plus grand que max2, max est égal à max1, sinon max est égal à max2
    if(max1 > max2):
        max = max1
    else:
        max = max2

    # Retourner la valeur de max
    return max

t = float(input("Entrez un nombre decimal >>> "))

print(f"Le nombre {t} au carré est {t**2}, sa racine carré est {t**(1/2)} et 1000 est {1000}.")
print(f"Quel est le plus grand ? La réponse est : {max4(t, t**2, t**(1/2), 1000)}")