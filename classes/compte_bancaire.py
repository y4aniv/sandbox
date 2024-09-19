class CompteBancaire:
    def __init__(self, id: int, owner: str, amount: str):
        """
        Constructeur de la classe CompteBancaire
        """
        self.__id = id
        self.__owner = owner
        self.__amount = amount

    def deposit(self, amount: int):
        """
        Méthode permettant de déposer de l'argent sur le compte

        Returns:
            int: le montant du compte après le dépôt
        """
        self.__amount += amount
        return self.__amount
        
    def withdraw(self, amount: int):
        """
        Méthode permettant de retirer de l'argent du compte

        Returns:
            int: le montant du compte après le retrait
        """
        self.__amount -= amount
        return self.__amount

    def transfer(self, amount: int, account):
        """
        Méthode permettant de transférer de l'argent d'un compte à un autre

        Returns:
            tuple: le montant du compte débiteur et du compte créditeur après le transfert
        """
        if(type(account) == CompteBancaire):
            self.withdraw(amount)
            account.deposit(amount)
        
        return self.__amount, account.__amount

    def __str__(self):
        """
        Méthode spéciale qui renvoie une représentation de l'objet sous forme de chaîne de caractères
        """
        return f"N°{self.__id}, {self.__owner}, {self.__amount}€"

accountTartempion = CompteBancaire(421, "Tartempion", 1500)
accountUntel = CompteBancaire(705, "Untel", 2000)

print(accountTartempion)
print(accountUntel)

assert accountTartempion.deposit(500) == 2000
assert accountUntel.withdraw(500) == 1500
assert accountTartempion.transfer(500, accountUntel) == (1500, 2000)
assert accountTartempion.transfer(500, accountUntel) == (1000, 2500)

print(accountTartempion)
print(accountUntel)