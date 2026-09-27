# Conditionals
# if, elif, else

age = int(input("Enter your age : "))

if age >= 18:
    print("You can Vote and Drive")
else:
    print("You can not vote and drive")


color = input("Enter color name : ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("look")
elif color == "green":
    print("go")
else:
    print("this color is invalid for traffic system.")

if age < 13:
    print("Child")
elif age >=13 and age < 18:
    print("Teenager")
else:
    print("Adult")

username = input("Enter username : ")
password = input("Enter password : ")

if username == "admin" and password == "1234":
    print("Login Successfull")
elif username != "admin":
    print("wrong username")
else:
    print("wrong password")

# how to check if number is multiple of a number or not

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

if num1 % num2 == 0:
    print(f"{num1} is divided by {num2} hence {num1} is multiple of {num2}")
else:
    print("Not a multiple")

# odd even

if num1 % 2 == 0:
    print("The number is Even")
else:
    print("Number is odd")

# nesting

username = input("Enter username : ")
password = input("Enter password : ")

if username == "admin" and password == "1234":
    print("Login successfull")
else:
    if username != "admin":
        print("wrong username")
    else:
        print("wrong password")

# match case

color = input("Enter a color")

match color:
    case "red":
        print("stop")
    case "yellow":
        print("look")
    case "green":
        print("go")
    case _: # this is the way to write default case
        print("Doesn't match")


# While loop example
count = 1
while count <= 10:
    print(count)
    count += 1

print()
print("After while Loop value of count is : ", count)
# Do not make a infinite loop, it will crash your system.

# loop to print numbers from 1 to 10

count = 1
while count <= 10:
    print(count)
    count += 1

# loop to print numbers in reverse order from 10 to 1

count = 10
while count >= 1:
    print(count)
    count -= 1

# table with the help of loop

num = int(input("Enter a number for its table: "))
i = 1
while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1

# if i = 0

i = 0
while i < 10:
    print(i * num)
    i += 1

# loops with break and continue
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

i = 1
while i <= 10:
    if i % 6 == 0:
        i += 1
        continue
    print(i)
    i += 1

i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

i = 1
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# for loop
string = input("Enter a string : ")
for char in string:
    print(char)

if 'o' in string:
    print("o is present in the string")

for var in range(10):
    print(var)

count = 0
string = "Artificial Intelligence"
for i in string:
    count += 1
print(f"Number of 'i' in the string: {count}")

# count the vowels in the string
word = input("Enter a word : ")
count = 0
for char in word:
    if char in "aeiouAEIOU":
        count += 1
print(f"Number of vowels in the word: {count}")

for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print(f"Number of vowels in the word: {count}")


# use of range() function in for loop

for i in range(1, 11, 1):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(1, 10, 2):
    print(i)

# so here we have learned about conditionals, loops, 
# and how to use them in Python. We also explored 
# the use of break and continue statements in loops, 
# as well as the match-case statement for pattern matching. 
# Additionally, we practiced counting characters and 
# vowels in strings using loops.

# printing sum of first 5 natural numbers
sum = 0
for i in range(1, 6):
    sum += i
print(f"Sum of first 5 natural numbers is: {sum}")

# printing sum of natural numbers from 1 to n
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"Sum of natural numbers from 1 to {n} is: {sum}")


# Now we will learn about functions
# functions are blocks of code that perform a specific task
#  and can be reused throughout the program. 
# They help in organizing code and making it more readable.

# function to print a greeting message
def greet(name):
    print(f"Hello, {name}! Welcome to the Python basics lesson.") # this is defination of the greet function which takes a parameter 'name' and prints a greeting message

greet("Alice") # this will call the greet function and pass "Alice" as an argument

def add_numbers(a, b):
    return a + b # this function takes two parameters 'a' and 'b' and returns their sum

result = add_numbers(5, 10) # calling the add_numbers function with arguments 5 and 10
print(f"The sum of 5 and 10 is: {result}") # printing the result

# taking input from user and using it in a function

def multiply_numbers(x, y):
    return x * y # this function takes two parameters 'x' and 'y' and returns their product

num1 = int(input("Enter first number: ")) # taking first number input from user
num2 = int(input("Enter second number: ")) # taking second number input from user
result = multiply_numbers(num1, num2) # calling the multiply_numbers function with the user inputs
print(f"The product of {num1} and {num2} is: {result}") # printing the result

# functions having default parameters

def add_numbers_with_default(a, b=10):
    return a + b # this function takes two parameters 'a' and 'b', where 'b' has a default value of 10  

result = add_numbers_with_default(5) # calling the function with only one argument, 'b' will take the default value of 10
print(f"The sum of 5 and default 10 is: {result}") # printing the
result = add_numbers_with_default(5, 15) # calling the function with both arguments
print(f"The sum of 5 and 15 is: {result}") # printing the result

# so difference between arguments and parameters is that
#  parameters are the variables defined in the function 
# definition, while arguments are the actual values 
# passed to the function when it is called.

# and non-default parameters are those that must be 
# provided when calling the function, while default 
# parameters have a predefined value and can be 
# omitted when calling the function. that is why non-default parameteres comes
#  first and default parameters comes after them in the function definition.



# now lets talk about built-in functions and user-defined 
# functions. Built-in functions are those that are already 
# defined in Python and can be used directly, 
# such as print(), len(), range(), etc. 
# User-defined functions are those that we create 
# ourselves to perform specific tasks, like the greet() 
# and add_numbers() functions we defined earlier.

# do you know i am talking to you virtual studio code and how you are predicting my code and giving me suggestions. It is because of the AI model which is trained on a large dataset of code and can understand the context of the code and provide suggestions accordingly. This is called code completion or code prediction. It helps developers to write code faster and with fewer errors.

# now we will create lambda fucntions. Lambda functions 
# are small anonymous functions defined using the lambda 
# keyword. They can take any number of arguments but can 
# only have one expression. The expression is evaluated 
# and returned when the function is called.

sum = lambda a, b : a + b # single line function to add two numbers

print(sum(5, 10))

mul = lambda a, b: a * b
print(mul(2, 6))

# higher order functions are those that can take other functions as arguments or return functions as results. Examples of higher-order functions in Python include map(), filter(), and reduce().

def calculate(func, a, b):
    return add_numbers(func(a, b), func(a, b)) # this function takes another function 'func' and two numbers 'a' and 'b' as arguments, and returns the sum of the results of calling 'func' with 'a' and 'b'

def func(x, y):
    return x * y # this function takes two numbers 'x' and 'y' and returns their product

result = calculate(func, 5, 10)
print(result)


# factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(6)
print(f"the result of factorial 6 is : {result}")

# using loops
def factorial_loop(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

result = factorial_loop(6)
print(f"the result of factorial 6 using loop is : {result}")

# this is the end of this file. In this file we have learned about conditionals, loops, 
# functions, lambda functions, higher order functions, and recursion. We have also seen 
# how to use these concepts in Python to solve problems and perform tasks.