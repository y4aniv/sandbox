# Portée des variables

### Exemple 1
Exécuter le programme P4_glob_loc1.py et répondre aux questions.

- Quelle erreur se produit ? 
    > La variable w n'est pas définie lors de l'affichage dans le print ligne 10
- Que peut on dire sur la variable w ?
    > La variable w est définie dans la fonction F1, c'est une variable locale
- A quoi sert cette variable ?
    > La variable w est utilisé pour être retourner par la fonction F1
- Combien de paramètres à la fonction F1 ?
    > La fonction F1 n'a aucun paramètres

### Exemple 2
Exécuter le programme P4_glob_loc2.py et répondre aux questions.

- Quel type de variable est x ?
    > Le type de la variable x est int
- Quel type de variable est a ?
    > Le type de la variable a est int
- La fonction F2 a-t-elle pu lire la valeur de a ?
    > La fonction F2 a pu lire la valeur de a

### Exemple 3
Exécuter le programme P4_glob_loc3.py et répondre aux questions.

- La variable globale a qui vaut 1 a-t-elle été modifiée par la fonction ? Pourquoi ?
    > La variable globale a qui vaut 1 n'as pas été modifié par la fonction F3 car elle a été modifier uniquement de manière locale
- Que dire de la variable a dans la fonction ?
    > La variable a dans la fonction est local

Rajouter en 1ère ligne de la fonction la commande :   global a
Puis exécuter à nouveau le programme.
> La variable a est devenue global et donc la variable a change de valeur pour tout le code à 100

### Cas particulier : une liste en paramètre
Exécuter le programme P4_glob_loc4.py et répondre aux questions.

- La variable L est-elle locale ou globale ?
    > Va variable L est locale
- Pourquoi la variable ma_liste est-elle modifiée, alors qu’on n’a pas écrit global ? 
    > Etant donner que la variable L contient une liste global, si une des valeurs de la liste change en local, la valeur de la site changera globalement