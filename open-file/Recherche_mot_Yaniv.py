def findWord(Word, file):
    """
    Fonction qui permet de rechercher un mot dans un fichier
    :entree: Word: str, file: str
    :sortie: None
    """
    assert Word != ""
    assert file != ""


    with open(file, 'r') as f:
        nLine = 0
        Result = False
        for line in f:
            Words = 0
            results = False
            if line.count(f"{Word} ") > 0:
                Words += line.count(Word)
                results = True
            if line.count(f"{Word},") > 0: 
                Words += line.count(Word)
                results = True
            if line.count(f"{Word};") > 0:
                Words += line.count(Word)
                results = True
            if line.count(f"{Word}.") > 0:
                Words += line.count(Word)
                results = True

            nLine = nLine+1
            if results == True:
                Result = True
                print(f"Le mot {Word} est présent {Words} fois dans la ligne {nLine} du fichier {file}")

        if Result == False:
            print(f"Le mot {Word} n'est pas présent dans le fichier {file}")
            

findWord('pas', 'Cyrano-UTF8.txt')
print("")
findWord('suis', 'Cyrano-UTF8.txt')
print("")
findWord('moral', 'Cyrano-UTF8.txt')