#                                   CLASSES AND OBJECTS

# class person:
#     name = "Moiz"
#     occupation = "Doing Nothing"
#     Networth = 10

# f = person()
# f.name = "Mansoori"
# f.occupation = "Python developer"
# print(f.name, f.occupation)

# class person:
#     name = "Moiz"
#     occupation = "Doing Nothing"
#     Networth = 10
#     def info(rost):
#         print(f"{rost.name} is {rost.occupation} ")

# a = person()
# b = person()
# c = person()
# b.name = "Mansoori"
# b.occupation = "Python developer"
# c.name = "Moiz Mansoori"
# c.occupation = "Software developer"
# a.info()
# b.info()
# c.info()


# class System:
#     def __init__(self , name  , department , Age):
#         self.name = name
#         self.department = department
#         self.Age = Age
    
#     def myfun(self ):
#         print(f"My name is {self.name} and I'am from {self.department} and my Age  is {self.Age}")

# ob1 = System( name = "Muzzamil" , department ="BSAI" , Age = "10")

# ob1.myfun()




# class Vehicle:
#     def __init__(self, Model , speed , year):
#         self.Model = Model
#         self.speed = speed
#         self.year = year

#     def myveh(self):
#         self.Model = input("Enter your Model :")
#         self.speed = input("Enter your Speed :")
#         self.year = input("Enter your Year :")

#     def prnt(self):
#         print(f"Model is {self.Model}\nAnd speed of Vehicle is {self.speed}\nAnd Year is {self.year}")

    
    
# p1 = Vehicle(Model = "self.model" , speed = "self.speed" , year = "self.year")
# p1.myveh()
# p1.prnt()











# CONSTRUCTION IN PYTHON --> 1) Parameterized constructor (2) Default Constructor
# constructor helps in creating an object sometimes, and in such cases, we want to pass arguments to create an object, and in those cases, the constructor helps us with some initialization.

# # Default Constructor

# class person:
#     def __init__(self):
#         print('Hey smile kro')
# a = person()

# Parameterized Constructor
# class person:
#     def __init__(self, name, occ):
#         print('Hey smile kro')
#         self.name = name
#         self.occupation = occ
#     def info(self):
#         print(f"{self.name} is {self.occupation} ")

# a = person("Moiz Mansoori", "Software developer")
# b = person("Mansoori", "Python developer")
# a.info()
# b.info()



# DECORATOR --> DECORATOR IS A FUNCTION THAT ACTUALLY TAKES ANOTHER FUNCTION AND EXTENDS THE BEHAVIOR OF THE LATTER FUNCTION.
# A decorator is a design pattern in Python that allows the user to add new functionality to an object without modifying its structure.

# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx

# def hello():
#     print("Hey BRO KEEP SMILEEEE")

# def add(a, b):
#     print(a + b)

# greet(hello)()  # <---- If using this, comment out the two lines above this comment.
# hello()

# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("Hey BRO KEEP SMILEEEE")

# def add(a, b):
#     print(a + b)

# hello()
# greet(add)(7, 9)


                        # GETTERS AND SETTERS
        # If you define a getter and try to set it in the setter, you need to use the setter's property.

# class myclass:
#     def __init__(self, value):
#         self._value = value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property
#     def value(self):
#         return self._value
# obj = myclass(18)
# obj.show()

# class myclass:
#     def __init__(self, value):
#         self._value = value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property
#     def ten_value(self):
#         return 10 * self._value
# obj = myclass(18)
# print(obj.ten_value)
# obj.show()

# class myclass:
#     def __init__(self, value):
#         self._value = value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property
#     def ten_value(self):
#         return 10 * self._value
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value / 10
# obj = myclass(18)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()



        # ACCESS SPECIFIERS/MODIFIERS (Access Specifier/Modifier)

# class employe:
#     def __init__(self):
#         self.__name = "Moiz"
# a = employe()
# print(a._employe__name)

# class student:
#     def __init__(self):
#         self._name = "Moiz"
#     def _fun(self):  # protected method
#         return "Mansoori"
# class subject(student):
#     pass
# obj = student()
# obj1 = subject()
# print(obj1._name)
# print(obj1._fun())
