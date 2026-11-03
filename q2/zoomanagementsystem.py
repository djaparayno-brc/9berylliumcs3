"""
Dexter Josue A. Parayno
9 - Beryllium
11/03/2026
"""

class Animal:                            # A parent class (Animal) is created.
    def __init__(self, name: str):       # Attributes (self, name) were initialized, with (name) expected to be a string.     
        self.name = name                 # An attribute (name) was created.

    def eat(self):                       # Method eat(self) created.
        print(f"{self.name} eats.")      # prints output as " _____ eats."

    def make_sound(self):                        # Method make_sound(self) created.
        print(f"{self.name} makes a sound.")     # prints output as "_____ makes a sound.

class Lion(Animal):                              # A child class Lion was made.
    def __init__(self, name: str):               # Attributes (self, name) initialized again, with (name) expected to be a string.
        super().__init__(name)                   # Attribute (name) inherited from the parent class Animal.             

    def make_sound(self):                        # Another method make_sound(self) created overriding that of the parent class.
        print(f"{self.name} roars loudly.")      # Output: "(name of the lion) roars loudly."

    def eat(self):                               # Another method eat(self) created overriding that of the parent class.
        print(f"{self.name} eats fresh meat.")   # Output: "(name of the lion) eats fresh meat."

class Elephant(Animal):                               # New child class Elephant created with Animal as its parent class.
    def __init__(self, name: str):                    # Attributes (self, name) initialized, with (name) expected to be a string
        super().__init__(name)                        # Attribute (name) inherited from the parent class Animal.

    def make_sound(self):                             # Another method make_sound(self) created overriding that of the parent class
        print(f"{self.name} trumpets.")

    def eat(self):                                    # Another method eat(self) created overriding that of the parent class.
        print(f"{self.name} eats grass and fruits.")

class Monkey(Animal):
    def __init__(self, name: str):                    # Attributes (self, name) initialized, with (name) expected to be a string
        super().__init__(name)                        # Attribute (name) inherited from the parent class Animal.

    def make_sound(self):                             # Another method make_sound(self) created overriding that of the parent class
        print(f"{self.name} chatters!")

    def eat(self):
        print(f"{self.name} eats bananas!")

# The main code
if __name__ == "__main__":
    # names were assigned to the classes Lion, Elephant, and Monkey
    lion = Lion("Simba")
    elephant = Elephant("Dumbo")
    monkey = Monkey("George")

    # Output proper:
    lion.make_sound()
    lion.eat()
    print("-----")
    
    elephant.make_sound()
    elephant.eat()
    print("-----")
    
    monkey.make_sound()
    monkey.eat()
    print("-----")
