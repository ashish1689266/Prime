# question 1
# Ask the user for a string and check whether it is a palindrome or not.Q1
# A palindrome is a string which is same when we read it forward & backward. Eg -
# “madam”, “racecar” etc

string1 = input("Enter a string to if it is palindrome or not : ")
start = 0
end = len(string1) - 1
print(len(string1))
is_palindrome = True
while start < end:
    print(string1[start], string1[end])
    if string1[start] != string1[end]:
        is_palindrome = False
    start += 1
    end -= 1
if is_palindrome == True:
    print("The string is palindrome")
else:
    print("The string is not palindrome")


# question 2
# Given a list of integers compute the average of all numbers in the list.
list1 = [34, 67, 74, 21, 22]
sum = 0
for num in list1:
    sum += num
print(f"The sum of list {list1} is {sum}")


# question 3
# Input two lists of integers from the user. Merge them into one list and sort the result
list1 = []
count = 0
while count < 5:
    list1.append(int(input("Enter a number: ")))
    count += 1

list2 = []
count = 0
while count < 5:
    list2.append(int(input("Enter a number: ")))
    count += 1

print(list1)
print(list2)
list1.extend(list2)
print(list1)
list1.sort()
print(list1)


# question 4
# Given a tuple of integers, create
# A tuple of all even numbers
# A tuple of all odd numbers

tuple1 = (34, 56, 2, 34, 89)
n = int(input("Enter an integer limit"))
tuple_even = ()
tuple_odd = ()
for i in range(0, n):
    if i % 2 == 0:
        tuple_even = tuple_even + (i,)
    else:
        tuple_odd = tuple_odd + (i,)
print(tuple_even)
print(tuple_odd) 


# question 5
#  Create a dictionary where
# Keys = student names
# Values = marks (integer)
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ)
# depending on the operation they want to perform on the dictionary
#A. Add a student
#B. Update marks
#C. Search for a student
#D. Display all students and marks

student_data = {
    "Ashish": 84,
    "Rohit": 79,
    "Nikita": 94,
    "Mark": 91,
    "Pallavi": 90
}

while True:
    print(student_data)
    print("A. Add a student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students and marks")
    choice = input("Enter a choice or 'exit' to quit.: ")
    if choice.lower() == "exit":
        print("Good bye!")
        break
    match choice:
        case 'A':
            name = input("Enter a name to update: ")
            marks = int(input("Enter marks: "))
            if student_data.get(name) == None:
                student_data.update({
                    name: marks
                })
                print("Record added")
                print(f"{name} : {student_data[name]}")
            else:
                print("This record already exist, add a new name or choose 'B' to update marks." )
        case 'B':
            name = input("Enter a name to search: ")
            marks = int(input("Enter marks: "))
            if student_data.get(name) != None:
                student_data[name] = marks
                print("Marks updated")
                print(f"Makrsks updated of {name} and is now {student_data[name]}")
            else:
                print("Record does not exist")
        case 'C':
            name = input("Enter a name to search: ")
            if student_data.get(name) != None:
                print(student_data[name])
            else:
                print("Record does not exist.")
        case 'D':
            for key, values in student_data.items():
                print(f"Marks of {key} is {values}")
        case _:
            print("Enter a valid choice.")
            


# question 6
# Create a dictionary that maps each word to its length.
word_dict = {}
i = 0
while i < 5:
    word = input("Enter a word: ")
    print(word_dict.get(word))
    if word_dict.get(word) == None:
        word_dict.update({
            word: len(word)
        })
        i += 1


# question 7
# Write a program that takes a string from the user and prints the number of
# spaces in the string

string = input("Enter a sentence: ")
count = 0
for char in string:
    if char == " ":
        count += 1
print(f"The count is spaces is {count}")


# question 8
# Write a program to check whether two lists share no common elements
list1 = [12, 65, 32, 45, 77]
list2 = [76, 87, 34, 45, 32]

set1 = set(list1)
set2 = set(list2)
if set1.intersection(set2) == set():
    print("The two set does not contains any common elements.")
else:
    print(f"The set contains common elements are {set1.intersection(set2)}")


# question 9
# Given a list, print all elements that appear more than once in the list
list1 = [2, 5, 7, 8, 6, 5, 2, 7, 5]
set_final = set()
set_dupulicate = set()
for num in list1:
    if num in set_final:
        if num in set_dupulicate:
            print(end="")
        else:
            set_dupulicate.add(num)
            print(f"{num} is the duplicate value and appear more than once.")
        
    else:
        set_final.add(num)


# question 10
# Ask the user for a string and print
# All unique characters
# The count of unique characters

string = input("Enter a string: ")
chara_set = set()
for char in string:
    if char not in chara_set:
        chara_set.add(char)
print(chara_set)
print(len(chara_set))


# this is the end of the homework 3