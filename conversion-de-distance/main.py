def miles(metre):
    """
    entree: metre (float)
    sortie: miles (float)
    """

    return metre / 1609.344
    
def metre(value, unit):
    """
    entree: value (float), unit (str)
    sortie: metre (float)
    """

    if(unit == "m"):
        return value
    elif(unit == "km"):
        return value * 1000
    elif(unit == "cm"):
        return value / 100
    elif(unit == "mm"):
        return value / 1000
    elif(unit == "um"):
        return value / 1000000
    else:
        return "Erreur: unité non reconnue"

def aire_disque(rayon, unit):
    """
    entree: rayon (float), unit (str)
    sortie: air (float)
    """

    return 3.141592653589793 * rayon**2 * metre(1, unit)**2

## miles(5000) # 3.106855961186669
## miles(220) # 0.13670133780487805
## miles(867) # 0.538767961186669

## metre(5000, "um") # 0.005
## metre(5000, "mm") # 5.0
## metre(220, "pcs") # Erreur: unité non reconnue

## aire_disque(5, "m") # 78.53981633974483
## aire_disque(200, "cm") # 12.566370614359172
## aire_disque(200, "pcs") # Erreur: unité non reconnue