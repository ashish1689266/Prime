# create a bankAccount class with attributes acount_number, owner name and balance
# add methods to deposit, withdraw and check balance

class bank_account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, add_amount):
        self.balance += add_amount
        print(f"{add_amount} INR deposited to account: {self.account_number}")

    def withdraw(self, subtract_amount):
        self.balance -= subtract_amount
        print(f"{subtract_amount} INR withdrawn from account: {self.account_number}")

    def check_balance(self):
        print(f"The bank amount for the name: {self.name}\n account_number: {self.account_number} is {self.balance} INR")

person1 = bank_account(101, "Ashish", 80_000)
person1.deposit(50_000)
person1.withdraw(25_000)
person1.check_balance()