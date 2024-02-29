# un DICTn'est pas une variable comme les autres !
# C'est un pointeur : sa valeur est une adresse mémoire

a = 1
b = a
a = 2
print(a)
print(b)

dico1 = {'Prénom': 'Eric', 'Age': 25, 'Taille': 1.82}
dico2 = dico1
dico3 = dico1.copy()

print("avant modif de dico1:")
print(dico1)
print(dico2)
print(dico3)

dico1['Prénom'] = "Alice"
print()
print("Après modif de dico1:")
print(dico1)
print(dico2)
print(dico3)

dico2.clear()
print()
print("Après modif de dico2 (vidé):")
print(dico1)
print(dico2)
print(dico3)
