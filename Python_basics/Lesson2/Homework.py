# Q1
# Write a program that takes salary as input. Using conditional statements,
# calculate the based on these rules:
# final tax rate
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

salary = int(input("Enter your salary : "))
if salary < 30000:
    print("The taxe rate will be :", 5, "%")
elif salary >= 30000 and salary <= 70000:
    print("The tax rate will be :", 15,"%")
else:
    print("The tax rate will be :", 25,"%")

# question 2
# Write a function that takes two integers and prints all even
# numbers between them (inclusive)

def print_even(a, b):
    for i in range(a+1, b):
        if i % 2 == 0:
            print(i)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print_even(num1, num2)


# question 3
# Write a function that prints the digits of a number,  n

def print_digits(n):
    while n > 0:
        digit = n % 10
        print(f"The digit is : {digit}")
        n //= 10

n = int(input("Enter a number : "))
print_digits(n)

# this question is star marked

# question 4
# Write a function to return the count the number of digits in a number, n

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

count = count_digits(int(input("Enter the number : ")))
print("The count of digits in the number is : ", count)


# question 5
# Write a function to return the sum of digits of a number, n

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += (n % 10)
        n //= 10
    return sum

print("The sum of digits of n is : ", sum_of_digits(int(input("Enter the number : ")))) 


# question 6
# Write a program to print all numbers from 1 to 100 that are divisible by both 3
# and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Number that is divisible by both 3 and 5 is : ", i)


# question 7
# Design a program to continuously input a number n from user & print if it is
# positive or negative until the user enters “Quit”.



while True:
    n = input("Enter a number to check positive or negative : ")
    if n == "quit":
        break
    if int(n) >= 0:
        print("The number is positive")
    else:
        print("The number is negative")


# question 8
# calculator function

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid Input"

result = calculator(10, 6, input("Choose one operator + , - , * , / : "))


# question 9
# prime number function

def is_prime(n):
    for i in range(2, n):
        if n % i != 0:
            continue
        else:
            return False
    return True

print("The number n is prime? ",is_prime(int(input("Enter a number to check a number is prime or not"))))


# question 10
# quessing game

number = int(input("Enter a number to be guessed : "))

while True:
    guess = input("Enter your guess : ")
    if int(guess) == number:
        print("Congratulations you guessed the number.")
        break
    elif int(guess) < number:
        print("Too low, guess a bigger number")
    elif int(guess) > number:
        print("Too big, guess a lower number")
    else:
        print("invalid input")

    # the homework id done for the class 2