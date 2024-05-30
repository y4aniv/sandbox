# PLUS PROCHES VOISINS a 2 dimensions - graphique FRUITS
# par Y.Adam en Python 3


import csv
import matplotlib.pyplot as plt



# corps du programme -----------------------------------------------------

# recuperation des donnees du fichier csv
with open("donnees_fruits.csv", "r", encoding='utf8') as fichier:
    table = list(csv.DictReader(fichier, delimiter = ";"))
    # table est une liste de DICTIONNAIRES, cles et valeurs sont des STR


# observation de la premiere donnee
print(table[0])


# element a classer
xE = 7.8
yE = 7.8


# creation du GRAPHIQUE
# creation des listes de donnees pour le graphique
xO = [float(d["largeur"]) for d in table if d["nom_fruit"] == "orange"]
yO = [float(d["hauteur"]) for d in table if d["nom_fruit"] == "orange"]
xC = [float(d["largeur"]) for d in table if d["nom_fruit"] == "citron"]
yC = [float(d["hauteur"]) for d in table if d["nom_fruit"] == "citron"]
xP = [float(d["largeur"]) for d in table if d["nom_fruit"] == "pomme"]
yP = [float(d["hauteur"]) for d in table if d["nom_fruit"] == "pomme"]
xM = [float(d["largeur"]) for d in table if d["nom_fruit"] == "mandarine"]
yM = [float(d["hauteur"]) for d in table if d["nom_fruit"] == "mandarine"]


# pour ajouter des cercles ou autre forme en plus du graphe
fig, ax = plt.subplots()

# ajout de cercle pour la distance euclidienne
ax.add_artist(plt.Circle((xE, yE), 0.3, edgecolor='blue', facecolor='none'))   # rayon 0.3
##ax.add_artist(plt.Circle((xE, yE), 0.5, edgecolor='red', facecolor='none'))
##plt.text(8.3, 7.6, "k=7 distance de Tchebytchev", color="blue")

# Ajout d'un rectangle pour la distance de Tchebychev
##ax.add_artist(plt.Rectangle((xE, yE), 0.8, 0.8, edgecolor = 'blue', facecolor = 'none'))

plt.axis('equal')  # pour un repere orthonorme, sinon le cercle sera une ellipse

# nuage de points
# Options de scatter : s = taille du point (20 par défaut),
# marker = symbole, 'o' : rond, 's' : carré , "D" : losange, "+", "x", "*" etc
plt.scatter(xO, yO, color="orange", label="orange", marker="o", s=18)
plt.scatter(xC, yC, color="yellow", label="citron", marker="v")
plt.scatter(xP, yP, color="green", label="pomme", marker="*")
plt.scatter(xM, yM, color="red", label="mandarine", marker="D", s=10)
plt.scatter(xE, yE, color="blue", label="à classer", marker="+")

plt.xlabel("largeur (cm)")
plt.ylabel("hauteur (cm)")
plt.title("Classification de fruits")
plt.legend(loc='lower right')

plt.show()

