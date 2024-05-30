import csv

dataset = open("iris_data_set.csv", "r", encoding='utf8')
dataset = list(csv.DictReader(dataset, delimiter = ","))

def dist_euclidienne(xA, yA, xB, yB):
    """
    Fonction qui permet de calculer une distance euclidienne entre deux points A et B
    
    Params:
        xA, xB : float
            Coordonnée x des points A et B
        yA, yB : float
            Coordonnée y des points A et B
    
    Return:
        float
            La distance euclidienne entre les points A et B
    """

    return ((xB - xA)**2 + (yB - yA)**2)**0.5

def dist_kppv(liste, k, x, y):
    """
    Fonction qui permet de calculer la distance entre un point et les k plus proches voisins
    
    Params:
        liste : list
            Liste des points
        k : int
            Nombre de plus proches voisins
        x, y : float
            Coordonnées du point
    
    Return:
        list
            Liste des k plus proches voisins
    """

    liste_dist = []
    for i in liste:
        dist = dist_euclidienne(float(i["petal_length"]), float(i["petal_width"]), x, y)
        liste_dist.append((dist, i["species"]))
    liste_dist.sort()
    return liste_dist[:k]

def nombre_kppv(liste, k, x, y):
    """
    Fonction qui permet de compter le nombre d'apparition de chaque classe

    Params:
        liste : list
            Liste des points
        k : int
            Nombre de plus proches voisins
        x, y : float
            Coordonnées du point
    
    Return:
        list
            Liste des k plus proches voisins
    """

    liste_kppv = dist_kppv(liste, k, x, y)
    classes = [classe[1] for classe in liste_kppv]
    classes_uniques = []
    for classe in classes:
        if classe not in classes_uniques:
            classes_uniques.append(classe)
    return [(classe, classes.count(classe)) for classe in classes_uniques]

def prediction(table, k, x, y):
    """
    Cette fonction permet de prédire la classe d'un point en fonction de ses k plus proches voisins

    Params:
        table : list
            Liste des points
        k : int
            Nombre de plus proches voisins
        x, y : float
            Coordonnées du point
    
    Return:
        str
            La classe du point
    """

    nombre_kppv_liste = nombre_kppv(table, k, x, y)
    nombre_kppv_liste.sort(key=lambda x: x[1], reverse=True)
    return nombre_kppv_liste[0][0]

assert round(dist_euclidienne(0, 0, 1, 1), 3) ==  1.414
assert dist_euclidienne(0, 1, 2, 1) == 2
assert dist_kppv(dataset, 3, 5.3, 1.5) == [(0.20000000000000018, 'virginica'), (0.22360679774997916, 'versicolor'), (0.2999999999999998, 'virginica')]
assert nombre_kppv(dataset, 3, 5.3, 1.5) == [('virginica', 2), ('versicolor', 1)]
assert prediction(dataset, 3, 5.3, 1.5) == 'virginica'