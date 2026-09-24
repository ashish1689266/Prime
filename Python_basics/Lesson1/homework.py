# Question1
# Write a program that asks the user for their name and age, then prints a
# sentence like:
# Q1
# Hello Shradha, you are 21 years old

name = input("Enter your name : ")
age = input("Enter your age : ")

print(f"Hello {name}, you are {age} years old")
print()
# Question 2
# Take two numbers as input from the user and print their sum, difference, product, and quotient

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
sum = num1 + num2
print("num1 + num2 = ", sum)

difference = num1 - num2
print("num1 - num2 = ", difference)

product = num1 * num2
print("num1 * num2 = ", product)

quotient = num1 / num2
print("num1 / num2 = ", quotient)

print()
# Question 3
# Ask the user to enter two integers and one float. Convert them all to floats and print their average

num1 = int(input("Enter first number in integer : "))
num2 = int(input("Enter second number in integer : "))
num3 = float(input("Enter a third number in float : "))

# Converting them all in float

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

average = (num1 + num2 + num3) / 3
print("The average if num1, num2 and num3 : ", average)


# Question 4
# The user enters a string containing a number (e.g., ). Convert it to:Q "45"
# • an integer
# • a float
# • a string again
# Print all three values with their types

string1 = input("Enter a number in string : ")
string_to_integer = int(string1)
print(string_to_integer)
string_to_float = float(string1)
print(string_to_float)
string2 = str(string_to_integer)
print(string2)

# Question 5
# Evaluate and print the result of the following expression

x = 10 + 3 * 2 ** 2
print(x)


# Question 6
# Write a program to swap values of two numbers entered by the user

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print()
print(num1, num2)

num2 = num1 + num2
num1 = num2 - num1
num2 = num2 - num1
print(num1, num2)


# Question 7
# Ask the user for a temperature in Celsius (string input). Convert it to float,
# then calculate and print temperature in Fahrenheit.
temp = input("Enter temperature in celsius : ")
temp = float(temp)

temp_in_fahrenheit = (temp * (9 / 5)) + 32
print()
print("Temperature in celsius is ", temp)
print("Temperature in Fahrenheit is : ", temp_in_fahrenheit)


# Question 8
# Take the radius (r ) as user input and print the area

pi = 3.14
radius = float(input("Enter radius : "))

area = pi * radius ** 2
print("Area of circle with radius ", radius, " is : ", area)


# Question 9
# Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and compute simple interest:

principal = input("Enter principal amount : ")
rate = input("Enter rate of interest : ")
time = input("Enter time in years : ")

print()
simple_interest = (float(principal) * float(rate) * float(time)) / 100
print("Simple interest is : ", simple_interest)


# Question 10
# ake a decimal number as input (like 47.68) and output its:

num1 = float(input("Enter a float number : "))
integer_part = int(num1)
fractional_part = num1 % integer_part
print()
print(integer_part)
print(fractional_part)