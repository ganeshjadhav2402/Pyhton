# del keyword
# Used to delete object properties or object itself
# del s1.name
# del s1
"""
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("ganesh")
print(s1.name)
del s1.name
print(s1.name)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Private(like) attributes & methods
# Conceptual Implementations in Python
# Private attributes & methods ate meant to be used only within the class and are not accessible from outside the class.
"""
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # "__"means this is private
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("65489723", "GSJ21")
print(acc1.acc_no)
print(acc1.reset_pass())
"""

"""
class Person:
    __name = "anonymous"
    
    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()
        
p1 = Person()
print(p1.welcome())
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Inheritence
# When one class(child/derived) derives the peroperties & methods of another class(parent/base). 
# Single Inheritance
"""
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("pirus")

print(car1.name)
print(car1.start())
"""

# Three Types Inheri: Single Inheritance, Multi-level Inheritance, Multiple Inheritance
# Multi-level Inheritance
"""
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()
"""

# Multiple Inheritance
"""class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"
    
class C(A, B):
    varC = "welcome to calss C"
    
c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Super Method 
# super() method is used to access methods of the parent class. 
"""
class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        
car1 = ToyotaCar("prius", "electrc")
print(car1.type)
"""

# class Method 
# A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can't access or modify class state & generally for utility.
"""
class Person:
    name = "anonymous"

    # def changeName(obj, name):
    #     self.__class__.name = "Rahul"
        
    @classmethod
    def changeName(cls, name):
        cls.name = name
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)  
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Property 
# We use @property decorator on any method in the class to use the method as a property 

"""
class Stud:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    
    @property   #latest value return method after new changes
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
        
stu1 = Stud(98, 85, 97)
print(stu1.percentage)

stu1.phy = 89
print(stu1.percentage)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  
# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meaning according to the context.

# Operator & Dunder functions: a+b(a.__add__b), a-b(a.__sub__b), a*b(a.__mul____b), 
# a/b(a.__truediv____b), a%b(a.__mod____b)

"""
print(1 + 2) #3 for nummbers
print(type(1))

print("ganesh" + "jadhav") #concatenate for strings
print(type("ganesh"))

print([1, 2, 3] + [4, 5, 6]) #merge for list
print(type([1, 2, 3]))
"""

# Opration Overloading for classes

"""
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
        
    def __add__(self, obj):
        newReal = self.real + obj.real
        newImg = self.img + obj.img 
        return Complex(newReal, newImg)
    
    def __sub__(self, obj):
        newReal = self.real - obj.real
        newImg = self.img - obj.img
        return Complex(newReal, newImg)
        
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

# num3 = num1 + num2 #for addition
# num3.showNumber()

num3 = num1 - num2 #for substraction
num3.showNumber()
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Let's Practice
# ◑ Qs. Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  #define area method
        return (22/7) * self.radius ** 2
    
    def perimeter(self):  #define perimeter method
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print("Circle Radius Area :",c1.area())
print("Circle Radius Perimeter :",c1.perimeter())
"""

# ◑ Qs. Define a Employee class with attributes role, department & salary. This class also 
# showDetails() method. Create an Engineer class that inherits properties from Employee & has additional name and age.
"""
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)
    
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")
        
engg1 = Engineer("Jeff Basos", 46)
engg1.showDetails()
# e1 = Employee("accountant", "Finance", "60,000")
# e1.showDetails()
"""

# ◑ Qs. Create a class called Order which stores item & its price.
#        Use Dunder function__gt__() to convey that:
#              order1 > order2 if price of order1 > price of order2
"""
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, odr2): #dunder function using __gt__
        return self.price > odr2.price
        
odr1 = Order("chips", 20)
odr2 = Order("tea", 10)

print(odr1 > odr2) #True  
"""













