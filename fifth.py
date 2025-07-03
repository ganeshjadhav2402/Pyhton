# Loops in Python
# Loops are used to repeat instructions.
"""
count = 1
while count <= 5:
    print("hello", count)
    count += 1

print(count)

i = 1
while i <= 1000:
    print("Ganesh", i)
    i += 1
"""

# Print Numbers from 1 to 5
"""
i = 1
while i <= 5:
    print(i)
    i += 1
"""

"""
i = 5
while i >= 1:
    print(i)
    i -= 1

print("Loop ended")
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Let's Practice
# ◑ Print numbers from 1 to 100
"""
num = 1
while num <= 100:
    print(num)
    num += 1
    
print("Print Ended")
"""

# ◑ Print numbers from 100 to 1
"""
num1 = 100
while num1 >= 1:
    print(num1)
    num1 -= 1

print("Loop Ended")
"""

# ◑ Print the multiplication table of a number n.
"""
n = int(input("Enter the n nummber: "))
i = 1
while i <= 10:
    print(n,"*",i,"=", n*i)
    i += 1 

print("Table is Created.")
"""

# ◑ Print the elements of the following list using a loop:
#     [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#traverse
idx = 0
while idx < len(nums):
    print(nums[idx]) #nums[0], nums[1], nums[2]...
    # print("On",idx,"index is",nums[idx]) #nums[0], nums[1], nums[2]...
    idx += 1
"""
    
# ◑ Search for a number x in this tuple using loop:
#     (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

"""
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter Search Number :"))

i = 0 #intiaization
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at index", i)
        break
    # elif(nums[i] != x):
    #     print("NOT FOUND")
    else:
        print("finding..")
    i += 1

print("end of loop")
"""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Break & Continue
# Break: used to terminate the loop when encountered.
"""
print("This is Break")
i = 0
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
"""

# Continue: terminates execution in the current iteration & continues execution of the loop with the next iteration.
"""
print("This is Continue")
i = 1
while i <= 10:
    # if(i % 2 == 0): #for ODD numbers
    if(i % 2 != 0): #for EVEN numbers
        i += 1
        continue #skip the number
    print(i)
    i += 1
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""













