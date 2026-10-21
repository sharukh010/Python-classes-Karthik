class Account: 
    def __init__(self,account): 
        if account == None:
            self.owner = "unknown"
            self.balance = 0 
        else: 
            self.owner = account.get_owner()
            self.balance = account.get_balance()
    def set_owner(self,new_owner): 
        self.owner = new_owner 
    def deposit(self,amount): 
        if amount <= 0: 
            print("Invalid amount")
        else: 
            self.balance += amount 
    def withdraw(self,amount): 
        if amount <= 0: 
            print("Invalid amount")
        elif amount > self.balance: 
            print("Insuficient balance")
        else: 
            self.balance -= amount 

    def get_owner(self): 
        return self.owner 
    def get_balance(self): 
        return self.balance
    def display(self): 
        print(f"Owner: {self.get_owner()}")
        print(f"Balance: {self.get_balance()}")

# account = Account(None)
# account.set_owner("Meena")
# account.deposit(500)
# account.withdraw(120)
# account.withdraw(900)
# backup = Account(account)
# backup.deposit(100)
# account.display()
# backup.display()
account = Account(None)
account.set_owner("Ravi")
account.deposit(250)
account.withdraw(250)
account.withdraw(1)
account.display()