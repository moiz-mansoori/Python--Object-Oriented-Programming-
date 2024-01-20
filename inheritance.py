
# IN OOP                # INHERITANCE (inheritance)  --> Inheritance allows us to reuse code by creating a new class that is a modified version of an existing class.
#                    <-- It enables us to change a class or create multiple classes in this program as demonstrated.

# # Base class
# class Employee:
#     def __init__(self, name, emp_id):
#         self.name = name
#         self.emp_id = emp_id

#     def show_details(self):
#         print(f"The detail of this person is ID: {self.emp_id} and the name is {self.name}")

# # Derived class
# class Programmer(Employee):
#     def function(self):
#         print("My default language is Gujrati")

# # Example Usage
# e = Employee("Moiz", 4200)
# e.show_details()
# e2 = Programmer("Mansoori", 3200)
# e2.show_details()
# # e2.function()

# # Another Derived class
# class Boys(Programmer):
#     def deffer(self):
#         print("My LOVE IS GONEEEEEEE!!!!!")

# # Example Usage
# e = Boys("Moiz", 4200)
# e.show_details()
# e2 = Programmer("Mansoori", 3200)
# e2.show_details()
# e2.function()
# e.deffer()



                # Single inheritance
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def sound(self):
#         print("Sound made by the animal")

# class DogBark(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="dog")
#         self.breed = breed

#     def sound(self):
#         print("Bark!")

# d = DogBark("dog", "dooggy")
# d.sound()
# a = Animal("dog", "dog")
# a.sound()

# # Quick quiz
# class Cat(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species='Cat')
#         self.breed = breed

#     def sound(self):
#         print("Meoowwww! Meowwwww!")

# b = Animal("cat", 'vat')
# b.sound()

# a = Cat("Cat", 'tat')
# a.sound()


#         # Multiple inheritance
# class Cricketer:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"The name of cricketer is {self.name}")

# class Business:
#     def __init__(self, businesses):
#         self.businesses = businesses

#     def show(self):
#         print(f"The name of business is {self.businesses}")

# class Both(Cricketer, Business):
#     def __init__(self, name, businesses):
#         Cricketer.__init__(self, name)
#         Business.__init__(self, businesses)

# b = Both("Moiz", 'Own business')
# print(b.name)
# print(b.businesses)
# b.show()
# print(Both.mro())



#         # Multilevel inheritance
# class Golden(DogBark):
#     def __init__(self, name, color):
#         DogBark.__init__(self, name, breed="Golden")
#         self.color = color

#     def show(self):
#         DogBark.show(self)
#         print(f"Color: {self.color}")

# a = Golden("Puppy", "Light White")
# a.show()
# print(Golden.mro())

            # Hierarchical inheritance

# # Base class
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def sound(self):
#         print("Sound made by the animal")

# # Derived classes
# class Dog(Animal):
#     def bark(self):
#         print("Woof! Woof!")

# class Cat(Animal):
#     def meow(self):
#         print("Meow! Meow!")

# # Example usage
# dog = Dog("Buddy", "Dog")
# cat = Cat("Whiskers", "Cat")

# dog.sound()  # Output: Sound made by the animal
# dog.bark()   # Output: Woof! Woof!

# cat.sound()  # Output: Sound made by the animal
# cat.meow()   # Output: Meow! Meow!




            # Hybrid Inheritance 

# # Base class
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def display_brand(self):
#         print(f"Brand: {self.brand}")

# # Class with Single Inheritance
# class Car(Vehicle):
#     def start_engine(self):
#         print("Engine started")

# # Class with Multiple Inheritance
# class ElectricCar(Car):
#     def charge_battery(self):
#         print("Battery charging")

# # Class with Multilevel Inheritance
# class LuxuryCar(ElectricCar):
#     def activate_massage_seat(self):
#         print("Massage seat activated")

# # Class with Hierarchical Inheritance
# class Bike(Vehicle):
#     def start_engine(self):
#         print("Bike engine started")

# # Class demonstrating Hybrid Inheritance
# class HybridVehicle(LuxuryCar, Bike):
#     def show_features(self):
#         print("Hybrid vehicle with multiple features")

# # Example usage
# electric_car = ElectricCar("Tesla")
# electric_car.display_brand()   
# electric_car.start_engine()      
# electric_car.charge_battery()    

# luxury_car = LuxuryCar("Mercedes")
# luxury_car.activate_massage_seat()  

# bike = Bike("Harley")
# bike.start_engine()              

# hybrid_vehicle = HybridVehicle("Volvo")
# hybrid_vehicle.display_brand() 
# hybrid_vehicle.start_engine()    
# hybrid_vehicle.charge_battery()  # 
# hybrid_vehicle.activate_massage_seat()  
# hybrid_vehicle.show_features()   
