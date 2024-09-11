class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        
    
    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print(f"You have deposited {deposit} amount")
    
    def withdraw(self, withdraw):
        self.balance = self.balance - withdraw
        print(f"You have withdrawed {withdraw} amount")
        
    def check_balance(self):
        print(f"Your current balance is: {self.balance}")
        
    
b1 = BankAccount(543245, 6992300, "11 september 2024", "Abdul Rahman Azam")
b1.deposit(1)
b1.withdraw(10000)
b1.check_balance()

b1.withdraw(5000000)
b1.check_balance()
