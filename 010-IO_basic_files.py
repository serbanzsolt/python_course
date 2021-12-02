# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:23:41 2021

@author: bfkhuser
"""

# =============================================================================
# Writing and Reading a TEXT FILE
# =============================================================================

# Writing 010_myfile.txt

myfile = open('Resources/010_myfile.txt')
print(myfile.read())
# When reading the file a cursor starts at the begining of the text
# and when it finishes it will be at the end, so it need to be reset.
myfile.seek(0)

contents = myfile.read()
print(contents)
myfile.seek(0)
readlines = myfile.readlines()
print(readlines)
print(type(readlines))

myfile.close()

# with statement

with open ('C:\\Projects\\python_course\\Resources\\010_myfile.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)
    my_new_file.seek(0)
    
with open ('Resources/010_myfile.txt', mode='r') as myfile:
    contents = myfile.read()
    print(contents)
    myfile.seek(0)
# with open ('Resources/010_myfile.txt', mode='w') as myfile:
#     contents = myfile.read()
# =============================================================================
# Reading, Writing, Appending modes
#  mode = 'r' - Read only
#  mode = 'w' - Write only (overwrite or create new)
#  mode = 'a' - Append only (will add on to files)
#  mode = 'r+' - Read and Write
#  mode = 'w+' - Write and Read (overwrite or create new)
# =============================================================================
print("\n")
with open ('Resources/010_myfile2.txt', mode='r') as f:
    print(f.read())
    f.close()
with open ('Resources/010_myfile2.txt', mode='a') as f:
    f.write('\nline 5')
    f.close()
    print("\n")
with open ('Resources/010_myfile2.txt', mode='r') as f:
    print(f.read())
    f.close()

# overwrite
with open ('Resources/010_myfile3.txt', mode='w') as f:
    f.write('I created this file')
    f.close()
