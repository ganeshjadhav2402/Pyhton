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

# Private(like) attributes & methods
# Conceptual Implementations in Python
# Private attributes & methods ate meant to be used only within the class and are not accessible from outside the class.
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # "__"means this is private
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("65489723", "GSJ21")
print(acc1.acc_no)
print(acc1.reset_pass())














