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


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # "__"means this is private
        
    
        
acc1 = Account("65489723", "GSJ21")
print(acc1.acc_no)
print(acc1.__acc_pass)














