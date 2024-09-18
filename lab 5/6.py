from abc import ABC, abstractmethod

class Employee(ABC):
    name = ""
    salary = 1

    @abstractmethod
    def calculateBonus(self):
        pass

class Manager(Employee):
    def hire(self):
        print("Manager is hiring someone")

    def calculateBonus(self):
        return self.salary * 20/100

class Developer(Employee):
    def writeCode(self):
        print("Developer is writing the code...")

    def calculateBonus(self):
        return self.salary * 10/100

class SeniorManager(Manager):
    def calculateBonus(self):
        return self.salary * 30/100
        
manager = Manager()
manager.name = "Alice"
manager.salary = 80000

developer = Developer()
developer.name = "Bob"
developer.salary = 60000

senior_manager = SeniorManager()
senior_manager.name = "Charlie"
senior_manager.salary = 100000

# Demonstrate functionality
manager.hire()
print(f"{manager.name}'s bonus: ${manager.calculateBonus()}")

developer.writeCode()
print(f"{developer.name}'s bonus: ${developer.calculateBonus()}")

print(f"{senior_manager.name}'s bonus: ${senior_manager.calculateBonus()}")
