Instruction: Do what is asked in each item below:
## 1. Answer the following questions:
### a. What is duck typing, as explained in the video?
- Duck Typing is a different way to do polymorphism besides using inheritance. It's basically the phrase, "If it looks like a duck and quacks like a duck, it must be a duck." In order for polymorphism to happen, the object needs to have the standard attributes or methods rather than relying formally on the class itself.
### b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class? 
-   It needed to have its own speak() method and alive attribute.

## 2. Create the Python code that:
- a. Creates three classes: Car, Boat, and Drone with a method move().
- move() in the Car class prints "The car drives on the road."
- move() in the Boat class prints "The boat sails on water."
- move() in the Drone class prints "The drone flies in the sky."
- b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the move() method: vehicle.move().
- c. Creates one object of each class.
- d. Calls the start_trip() method for each object.
```python
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)
```
## 3. How does the code in 2.2 demonstrate polymorphism?
- From the term "many forms," the code demonstrates polymorphism because the method move() is repeated across different classes. This type of polymorphism is called method overriding.
