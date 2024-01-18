data = ["Harry Potter", "La Casa de Papel", "Kim Kardashian"]

while True:
    entry = input('Ajouter un élément >>> ')

    isNew = True
    toAdd = True

    if entry == "stop":
        print("Au revoir...")
        print("--------------------------------------------")
        print(data)
        print("--------------------------------------------")
        exit()

    for n in range(len(data)):
        if data[n] == entry:
            print(f"L'élément {entry} est déjà enregistré à la position {n}")
            isNew = False

    if isNew == False:
        toAdd = input("Voulez vous le rajouter (y/n) >>> ")

        if toAdd.lower() == "y":
            toAdd = True
        else:
            print(f"L'élément {entry} n'a pas été enregistré")
            toAdd = False

    if toAdd:
        data.append(entry)
        print(f"L'élément {entry} a été enregistré")