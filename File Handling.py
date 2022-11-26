# Ways of identifying errors
"""
Output-Terminal
Try and except blocks (exception handling)
Debugging
"""
# How to handle Files
"""
open() - to open file
"r" - read the file
"a" - make an append to the file
"w" - write to the file
"x" - create a  file
"t" - text mode [the default mode]
"b" - binary [images]
close() - close the file

{to open} f = open("Short poem.txt", "r")
print(f.read(4))

f = open("Short poem.txt", "w")
f.write("This is my poem")
f.close

f = open("Short poem.txt", "a")
f.append("It's a short poem")doesn't work(write first and append)
"""
f = open("Hope.txt", "r")
print(f.read())
