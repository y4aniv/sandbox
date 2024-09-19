class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octet(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        return self.adresse == "192.168.0.0" or self.adresse == "192.168.0.255"

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l’adresse self
        si elle existe et False sinon"""
        octets = self.liste_octet()
        if octets[3] < 254:
            
            octet_nouveau = octets[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False
        
adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')

assert adresse1.est_reservee() == False
assert adresse3.est_reservee() == True
assert adresse2.adresse_suivante().adresse == '192.168.0.3'