class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code
        
        
    def printdata(self):
        print(f"The account number is: {self.__account_no}\nThe account balance is: {self.__account_bal}\nThe Security_code is: {self.__security_code}")
        
        
        
a = Account(1234,5000,2024)

a.printdata()
