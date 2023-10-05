# Fonction F3 nous permettant de tester la portée des variables
# par Y.ADAM en Python 3

def F3():
    global a
    a = 100
    return a

a = 1
print("A l'exterieur, avant l'appel a = " + str(a) )
print("La fonction F3 retourne a qui vaut ", F3() )
print("A l'exterieur, apres l'appel, a = " + str(a) )


