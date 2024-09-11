class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
        print(f"The seating capacity is {self.seating_capacity}")
        
    def total_fare(self):
        return self.seating_capacity * 100
    
    
class Bus(Vehicle):
    def calculate_fare(self):
        bus_fare = super().total_fare()
        
        maintenance_charge = bus_fare * 0.10
        
        total_fare = bus_fare + maintenance_charge
        
        return total_fare
        
        
b = Bus(20)
print(f"The total bus fare is : {b.calculate_fare()}")
