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

import os
os.remove("sample.txt")


















































































































































































































































































































