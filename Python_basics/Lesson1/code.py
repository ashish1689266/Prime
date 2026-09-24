print("Hello World","\n", "Apna College")
print("Well done your code is good")


print()
# Variables

name = "Ashish Kumar"
age = 27
height = 170.5

print(name)
print("Age is:", age)
print("Height is:", height - 0.5)

# Rules of naming the variables is use alphabets, numbers, _ but do not start with numbers

print()
# types of variables we have is 4
# int, float, boolean, string, nonetype

count = 5
margin = 18.4
nameItem = "Laptop"
isavalaible = True

isValue = None

# you can print their type as well with type() function 

print(type(count))
print(type(margin))
print(type(nameItem))
print(type(isavalaible))
print(type(isValue))

# Now you have to understand about keywords in python these are reserved words and you will learn about them in the process so do not worry
# secondly we have to understand about the style guide, there is a proper way to write different variables
# first is snake case 

my_variable = 6

# second is camel case 
myVariable = 6

# third is pascal case
MyVariable = 6

# from now on we will follow the snake_case evry time 

# add two numbers 

a = 10
b = 20

sum = a + b
print()
print("sum is - ", sum)

# now we discuss about the operators and oprands here in this example a and b are oprands
#  and + symbol and = symbol are operator
# arithmetic operators
# so now we do rest of basic calculations
print()
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # this is floor division only give you the largest integer smaller or equal to the number
print(a % b) # this is modulo it calculates the remainder after division
print(a ** b) # this is power operator this means a to the power b


# now we have some relational and comparision operators

# if you ask a question you will get True or False here
print()
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
#  when you print these you will answers in True and False 

# now we have assignment operators

a = 15

a = a + 5

# this statement can be written like
a += 5
# this is same as the above one, so this is a short cut for this and it can be applied on every mathematical operator here
# and these are our different assignment operator

print()
a -= 5
print(a)
a *= 5
print(a)
a /= 5
print(a)
a //= 5
print(a)
a %= 5
print(a)
a **= 5
print(a)

# so now here comes our logical operators they are not, and , or 
# when you need opposite of the answer then use this like
print()
print(not False)
print(not True)
print(not a) # here value of a is not zero so it will say True but not will reverse it
a = 0
print(not a) # here value will be False because of zero but not will reverse it

# then we have and operator which applies over two or more than two conditions like
print(a > 8 and a == 10) # here we have two conditions and "and" is applied here, if both are true then you get true otherwise false
print(a < 4 and a == 0)

# now we have or operator it is same to and but it will give you True when any of the 
# conditions will give you true or all the conditions are True,
#  in only one case it gives you False, when all the conditions are False 

print(a < 7 or a > 4)
print(a < 0 or a != 0)

# now we will talk about type conversion, so we can convert the data types into each 
# other only when it is compatible like int to float, float to int, string to int and int to string
# and int to bool

a = 10
a = float(10)
a = int(4.5)
a = int("123")
a = str(123)
a = bool(0)
a = bool(12)
print()
# just like this, but this is what we can do and this is explicit type conversion
# so we also have implicit type conversion that interpreter does on its own like
a = 10
print(type(a))
a = a + 4.5 # so here int plus float is float so no data will be lost and size of float is bigger than int so it converts the answer into float even when type of a is int earlier
print(type(a))

# now this lectures last part is how to interact with user 
# this is done with the help of input function here we can use it to take users value and do computation on it
print()
a = input("Enter a number : ")
b = input("Enter a number : ")
sum = a + b # this just add the characters like 10 + 5 = 105 which is wrong 
# because input naturally stores in string
print(sum)
# so we have to do type conversion
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
sum = a + b
print(sum)

print()
# so after learning all this we will calculate average of two numbers
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

avg = num1 + num2 / 2 # this looks correct but will give wrong answers because of operator prcedence
print(avg)

avg = (num1 + num2) / 2 # this is correct because now addition takes place first as it is inside a parenthesis.
print(avg)