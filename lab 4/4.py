class Employee:
    
    def get_data(self):
        self.name = input("Enter your name")
        self.salary = int(input("Enter your salary"))
        self.taxpercent = int(input("Enter tax percentage"))
        
    def Salary_after_tax(self):
        self.salary = self.salary - (self.salary * 2 / 100)
        
    def update_tax_percentage(self):
        if(self.taxpercent < 100)
            self.taxpercent = self.taxpercent + 1
            

e = Employee()
