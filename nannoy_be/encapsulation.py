class Wallet :
    def __init__(self,balance):
        self._balance = balance

    #track if the amount is a non-positive amount 
    def valid_amount(self,amount):
        if amount < 0 : 
            raise ValueError('Error.Amount must be positive')        

    def deposit(self,amount):
        self._valid_amount = amount
        if amount > 0:
            self._balance += amount 

    def withdraw(self,amount):
        self._valid_amount = amount
        if amount > self._balance :
            raise ValueError("Insufficient funds")
        self._balance -= amount             

    def get_balance(self):
        return self._balance 

    def __str__(self):
        return f"balance = {self._balance}"

    


account = Wallet(1000)
account.deposit(50)
print(account)

account_1 = account 
account_1.withdraw(200)
print(account_1)


class BankAccount:# Class with encapsulation
    def __init__(self, balance):
        self.__balance = balance # attribute: private

    def get_balance(self): # Public method
         return self.__balance




account = BankAccount(8000)

print(account.get_balance()) # Access through method

# print(account.__balance)    # Attribute can't be accessed directly