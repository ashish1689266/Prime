# now we will work on different modes of file 
# r mode and w mode we have already seen

# x mode is used to create new files 
file1 = open("data.txt", "x")

file1.write("Hello world")
file1.close()
file1 =open("data.txt", "r")
data = file1.read()
print(data)
file1.close()

# a mode this is used to write with truncating
file1 = open("data.txt", "a")
file1.write("\nThis is new world")
file1.close()

file1 = open("data.txt", "r")
data = file1.read()
print(data)
file1.close()

# now we can combine these modes with each other
# rt - to open file in read text mode
# rb - to open file in read binary mode, this binary can also be used alone and it is for media files because they are not text
# wt - to open file in write text
# wb - to write the binary files
# r+ - with this you can read and write but the pointer is at the starting so whatever you will write will overright the text from stating
# w+ - with this you can read and write but pointer is at the start of the text but before this it will truncate the whole file
# a+ - with this you can read and write but pointer is at the end of the file and you can read and write at end but this will not truncate it as it is append

# now we have to close a file every time to make it safe but mistakes can happen, intentionally or not

# here we will use with keyword

with open("data.txt", "r") as file1:
    data = file1.read()
    print(data)

# with this it will do the work and then close it after


# now finally how to delete a file
# we use operating system library and methods of it
import os

os.remove("data.txt") # this is how we delete the path