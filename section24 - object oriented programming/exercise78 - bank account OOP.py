class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
    
    def deposit(self, val):
        self.balance += val
        return self.balance
    
    def withdraw(self, val):
        self.balance -= val
        return self.balance