class Account:
    """ This is the class to create a basic default account object"""

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.commit()

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """ This class creates checking account objects"""

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        self.commit()


account = Account("balance.txt")
print(account.balance)


checking = Checking("balance.txt", 2)
checking.transfer(108)

print("Checking: " + str(checking.balance))
