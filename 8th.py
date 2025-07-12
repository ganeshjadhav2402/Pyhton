# OOP in Python
# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming.

# Class & Object in Python

"""
#creating class
class Students:
    name = "Kran Kumar"
    def __init__(self):
        print(self)
        print("adding new students in Database...")
    
# creating objects
s1 = Students()
# print(s1)
"""

# s2 = Students()
# print(s2.name)


"""
class Car:
    brand = "BMW"
    color = "Blue"
    model = "BMW i5 M60 xDrive"

c1 = Car()
print("Color of Car :",c1.color)
print("Brand of Car :",c1.brand)
print("Model of Car :",c1.model)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Constructor: All classes have a function called __init__(), which is always executed when the object is being
# initiated.
# *The self parameter is a reference to the current instance of the class, and is used to access variables
# that belongs to the class.

"""class Students:
    
    
    #default constructors
    def __init__(self):
        pass   
     
        
    #parameterized constructors
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in Database...")
    
# creating objects
s1 = Students("Karan", 97)
print(s1.name, s1.marks) #Karan

s2 = Students("Mahesh", 85)
print(s2.name, s2.marks)"""

# Class & Instance Attributes
# Class.attr
# obj.attr

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Methods
# Methods are functions that belong to objects

# creating class
"""
class Students:
    college_name = "Naran Lala College"
        
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("welcome student,", self.name, "Your Marks is", self.marks)
        
    def get_marks(self):
        return self.marks
    
s1 = Students("Karan", 98)
s1.welcome()
print(s1.get_marks())
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Let's Practice
# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hello", self.name, "your avg score is:", sum/3)
        
s1 = Student("Steave",[98, 85, 90])
s1.get_avg()
        
s1.name = "Captain AM" #as per in future you chnaged attribute value
s1.get_avg()
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Static Method
# Methods that don't use the self perameter(work at class level)

"""
class Static:
    @staticmethod  #decorator
    def college():
        print("ABC College")
"""
        
# *Decorators allow us to wrap another functionin order to 
# extend the behaviour of the wrapped function, without permanently modifying it 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Important
# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user.
"""
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started..")

car1 = Car()
car1.start()
"""

# Encapsulation
# Wrapping data and functions into a single unit(objects).

# Let's Practice
# Create Account class with 2 attributes - balance & aacount no.
# Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
        print("total balance = ", self.get_balance())
    
    #debit method
    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was credited")
        print("total balance = ", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 658974235)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)

print("Account Balance :",acc1.balance)
print("Account Number  :",acc1.account_no)







