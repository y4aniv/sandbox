# affichage d'une matrice
# en Python 3

matrice = [["5", "3", "1"],
           ["6", "2", "9"],
           ["4", "8", "7"]]

print("un affichage pas très beau :")
print(matrice)
print()

print("un affichage plus lisible, pas parfait cependant :")
for row in matrice:
    print(" ".join(row))
print()

print("un bel affichage, sans apostrophe, avec espace séparateur:")



