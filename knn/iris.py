import csv 
import matplotlib.pyplot as plt

with open("iris_data_set.csv", "r", encoding='utf8') as fichier:
    table = list(csv.DictReader(fichier, delimiter = ","))

petal_length = float(input("Entrer la longueur du pétale : "))
petal_width = float(input("Entrer la largeur du pétale : "))

xSetosa = [float(d["petal_length"]) for d in table if d["species"] == "setosa"]
ySetosa = [float(d["petal_width"]) for d in table if d["species"] == "setosa"]
xVersicolor = [float(d["petal_length"]) for d in table if d["species"] == "versicolor"]
yVersicolor = [float(d["petal_width"]) for d in table if d["species"] == "versicolor"]
xVirginica = [float(d["petal_length"]) for d in table if d["species"] == "virginica"]
yVirginica = [float(d["petal_width"]) for d in table if d["species"] == "virginica"]

fix, ax = plt.subplots()

ax.add_artist(plt.Circle((petal_length, petal_width), 0.3, edgecolor='blue', facecolor='none'))

plt.axis('equal')

plt.scatter(xSetosa, ySetosa, color="orange", label="setosa", marker="o", s=18)
plt.scatter(xVersicolor, yVersicolor, color="yellow", label="versicolor", marker="v")
plt.scatter(xVirginica, yVirginica, color="green", label="virginica", marker="*")
plt.scatter(petal_length, petal_width, color="blue", label="à classer", marker="+")

plt.xlabel("longueur du pétale (cm)")
plt.ylabel("largeur du pétale (cm)")
plt.title("Classification de fleurs")
plt.legend(loc='lower right')

plt.savefig("iris.png")