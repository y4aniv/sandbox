# programme de pavage d'un rectangle par des carres
# avec graphique tkinter
# en Python 3, d'apres S.Tummarello


from tkinter import *


# fonctions graphiques

def affiche_rectangle(x_, y_, w_, h_, col='yellow', margin=(100, 20)):
    """ affiche un rectangle avec sa hauteur affichee au centre, dans une fenetre tkinter
    entree: largeur w (int), hauteur h (int), coordonnees x et y (int) du coin superieur gauche
    """
    global zoom
    zoom = 20
    x = x_*zoom
    y = y_*zoom
    w = w_*zoom
    h = h_*zoom
    canvas.create_rectangle(margin[0]+x, margin[1]+y, margin[0]+x+w, margin[1]+y+h, fill=col, outline='black')
    canvas.create_text(margin[0]+x+w/2, margin[1]+y+h/2, text=str(h_), justify='center')



def affiche_carre(x, y, c):
    """affiche un carre c'est a dire un rectangle avec 2 cotes egaux
    entree : int, int, int
    """
    COULEURS = ['#d9ed92', '#b5e48c', '#99d98c', '#76c893', '#52b69a', '#34a0a4', '#168aad', '#1a759f', '#1e6091', '#184e77']
    affiche_rectangle(x, y, c, c, col=COULEURS[c % len(COULEURS)])

def affiche():
    """ remet a jour la fenetre en affichant le rectangle et les carres
    """
    w = int(spin_w.get())
    h = int(spin_h.get())
    carres = calcule_liste_carres(w, h)
    canvas.delete("all")

    for carre in carres :
        x,y,c = carre 
        affiche_carre(x, y, c)

    canvas.create_rectangle(100, 20, 100+w*zoom, 20+h*zoom, outline='black', fill='white')

# calcul

def calcule_liste_carres(w, h):
    carres = []     # creation de la liste des carres
    x = 0
    y = 0
    reste_w = w
    reste_h = h

    while reste_w > 0 and reste_h > 0:
        # Trouver la taille du plus grand carré possible
        c = min(reste_w, reste_h)

        # Ajouter le carré à la liste
        carres.append((x, y, c))

        # Mettre à jour les coordonnées et l'espace restant
        if reste_w > reste_h:
            x += c
            reste_w -= c
        else:
            y += c
            reste_h -= c

    return carres



# programme principal ----------------------------


# affichage de la fenetre

fen = Tk()  # creation d'un objet de type fenetre tkinter

lab_w = Label(fen, text='LARGEUR', bg='white', fg='blue')
lab_w.pack()

spin_w = Spinbox(from_=1, to=40, increment=1, command=affiche)
spin_w.pack()

lab_h = Label(fen, text='HAUTEUR', bg='white', fg='blue')
lab_h.pack()

spin_h = Spinbox(from_=1, to=30, increment=1, command=affiche)
spin_h.pack()

canvas = Canvas(fen, width=1000, height=700)
canvas.pack()

fen.mainloop()