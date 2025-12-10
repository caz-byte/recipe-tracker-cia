class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds") 
Acc = BankAccount ("gabriel")
print (Acc.owner)
Acc.deposit(9000)
Acc.withdraw (10000)