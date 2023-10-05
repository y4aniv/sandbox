# Fonction nous permettant de tester la portee des variables
# par Y.Adam, en Python 3


def double_list(L):
    """fonction qui multiplie par 2 tous les elements d'une liste
    List --> none """
    n = len(L)
    for i in range(n):
        L[i] = 2*L[i]


ma_liste = [10, 20, 30]

print("Avant l'appel ma liste est ", ma_liste)

double_list(ma_liste)

print("Apres l'appel ma liste est ", ma_liste)
