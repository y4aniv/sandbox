# manipulations de fichiers textes en Python 3
# par Y. Adam


###### pour afficher le contenu du fichier entier

fichier = open("Cyrano-UTF8.txt","r")    # on ouvre en mode "read" : lecture
poeme = fichier.read()            # on stocke dans une variable le contenu entier
fichier.close()
print(poeme)
print()


###### pour afficher le contenu du fichier ligne par ligne

f = open("Cyrano-UTF8.txt","r")
for ligne in f:
    print(ligne)
f.close()
print()



##### pour afficher une partie du contenu du fichier

fichier = open("Cyrano-UTF8.txt", "r")
extrait1 = fichier.read(10)       # on stocke les 10 premiers caracteres
print(extrait1)

extrait2 = fichier.read(8)       # puis les 8 caracteres suivants
print(extrait2)

ligne = fichier.readline()      # lit la ligne a partir du curseur et saute une ligne
print(ligne)
ligne = fichier.readline()
print(ligne)
fichier.close()



######### pour ajouter du texte dans un fichier

g = open('ploc.txt', 'a')        # ouvre le fichier 'ploc' en mode "append"
g.write("ajout de texte")
g.write("\n")   # va a la ligne
g.close()



######### pour ecrire en remplacant le contenu du fichier

a = 25001
b = 1998
h = open('scores.txt', 'w')
h.write("Scores des joueurs :\n")
h.write("Alice : " + str(a) + "\n")
h.write("Bob : " + str(b) + "\n")
h.close()


