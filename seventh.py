# File I/O in Python
# Python can be used to perform operations on a file. (read & write data)
# Type of files
# 1. Text Files: .txt, .docx, .log etc.
# 2. Binary Files: .mp4, .mov, .png, .jpeg etc.

"""
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()
"""

# Reading a file 
"""
data = f.read() #read entire file
data = f.readline() #reads one line at a time
"""

# Wrting to a file
"""
f = open("demo.txt", "w")    
f.write("Ganesh JAdhav from NAvsari. \nAll of Us are Dead") 
"""

"""
f = open("demo.txt", "a")
f.write("\nthis is new line for file.")
"""

"""
f = open("sample.txt", "w")
f.write("NEw Sample File Here.")
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Charater                Meaning
# 'r'          open for reading (default)
# 'w'          open for writing, truncating the life first               
# 'x'          create a new file and open it for writing
# 'a'          open for writing, appending to the end of the file if it exist
# 'b'          binary mode
# 't'          text mode (default)
# '+'          open a disk file the updating (reading and writing) 
# 'r+'         read+ overwrite exsting data (pointer start) - no truncate
# 'w+'         read, overwrite exsting data                 - truncate
# 'a+'         read, append    exsting data (pointer end)   - no truncate

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# with Syntax 
"""
with open("demo.txt", "r")as f:
    data = f.read()
    print(data)

with open("demo.txt", "w")as f:
    f.write("new data from laptop added")
"""

# Deleting a File
# using the os module
# Module (like a code library) is a file written by another programmer that generally has
# a functions we can use.

"""
import os
os.remove("sample.txt")
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Let‘s Practice
# Create a new file “practice.txt” using python. Add the following data in it:
"""
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O ")
    f.write("using Java. \nI like programming in Java.")
"""

# WAF that replace all occurrences of “java” with “python” in above file.
"""
with open("practice.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)
"""

# Search if the word “learning” exists in the file or not.
"""
# using Function 
def check_word():
    word = "xlearning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("FOND")
        else:
            print("NOT FOUND")

check_word()
"""

# using without Function
"""
word = "xlearning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("FOND")
    else:
        print("NOT FOUND")
"""

# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.
# using Function 
"""
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("FOND")
        else:
            print("NOT FOUND")

def check_for_line():
    word = "PYQ"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())
"""

# From a file containing numbers separated by comma, print the count of even numbers.
"""
with open("pratice2.txt", "w") as f:
    f.write("1, 4, 85, 45, 66, 90")
"""

# numbers separated by comma
"""
with open("pratice2.txt", "r") as f:
    data = f.read()
    print(data)
    
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
"""

# print the count of even numbers
count = 0

with open("pratice2.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
            
print(count)









