class Account:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, dep):
        self.balance += dep
        print("Deposit Accepted")
    
    def withdraw(self, wit):
        if (wit > self.balance):
            print("Funds Unavailable")
        else:
            self.balance -= wit
            print("Withdrawal Accepted")
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    
acct1 = Account('Jose', 100)

print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)

