

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)

    def __str__(self):
        return f'Owner: {self.owner}, Balance: {self.balance}'

    def display(self):
        print(self)


alice = BankAccount('Alice', 5000)
bob = BankAccount('Bob', 2000)
alice.display()
bob.display()

#deposit money in alice account
alice.deposit(500)
alice.display()

#tranfer balance from alice to bob of amount 2500
alice.transfer(bob, 2500)
alice.display()
bob.display()