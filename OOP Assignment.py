
class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.available = True
    
    def markAvailability(self, availability):
        self.available = availability

    def IsAvailable(self):
        print(f"{'Available for Viewving' if self.available else 'In Quarantine'}")

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Habitat: {self.habitat}, "

class Mammal (Animal):
    def __init__(self, name, age, habitat, furLength, diet):
        super().__init__(name, age, habitat)
        self.furLength = furLength
        self.diet = diet 
    
    def display(self):
        return super().display() + f"Fur Length: {self.furLength}, Diet: {self.diet}"


class Bird (Animal):
    def __init__(self, name, age, habitat, wingspan, flyAltitude):
        super().__init__(name, age, habitat)
        self.flyAltitude = flyAltitude
        self.wingspan = wingspan

    def disdisplay(self):
        return super().display() + f"Wingspan: {self.wingspan}, Fly Altitude: {self.flyAltitude}"

class Reptile (Animal):
    def __init__(self, name, age, habitat, scalePattern, venomous):
        super().__init__(name, age, habitat)
        self.scalePattern = scalePattern
        self.venomous = venomous

    def display(self):
        return super().display() + f"Scale Pattern: {self.scalePattern}, Venomous: {self.venomous}"



def main():
    lion = Mammal(name="Lion", age=5, habitat="Savannah", furLength="Short", diet="Carnivore")
    eagle = Bird(name="Eagle", age=3, habitat="Mountains", wingspan=2.3, flyAltitude=2000)
    snake = Reptile(name="Snake", age=2, habitat="Rainforest", scalePattern="Striped", venomous="Yes")

    lion.markAvailability(False)
    eagle.markAvailability(True)
    snake.markAvailability(True)

    print("=== Zoo Animals Information ===")
    print(lion.display())
    lion.IsAvailable()
    
    print(eagle.display())
    eagle.IsAvailable()
    
    print(snake.display())
    snake.IsAvailable()

if __name__ == "__main__":
    main()


