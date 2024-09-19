class SalleLycee():
    def __init__(self, floor: int, door: int, capacity: int, hasComputeurs: bool):
        self.floor = floor
        self.door = door
        self.capacity = capacity
        self.hasComputeurs = hasComputeurs

    def changeToInformatics(self):
        # Méthode mutatrice
        self.hasComputeurs = not self.hasComputeurs

salle_721 = SalleLycee(7, 21, 24, True)
salle_720 = SalleLycee(7, 20, 35, False)

salle_721.changeToInformatics()
assert salle_721.hasComputeurs == False