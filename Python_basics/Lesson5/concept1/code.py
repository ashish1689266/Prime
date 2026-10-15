# now we will start learning about file input/output

# to take the input of a file you have to use open() and inside give file path and modes as read and write
#

file1 = open("data.txt", "r") # first is path and second is r- read

# now we will save the text from this file in a variable
data = file1.read()

# now we can print it 
print(data)

# we can read file line by line
data = file1.readline()
print(data)

data = file1.readline()
print(data)

data = file1.readline()
print(data)

data = file1.readline()
print(data)

file1.close() # this is important to close this file

# now we can write into this file
file1 = open("data.txt", "w")
file1.write("Hi")
# data = file1.read()
# print(data)
file1.close()

file1 = open("data.txt", "r")
data = file1.read()
print(data)