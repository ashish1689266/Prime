# In this lesson we will work on strings

# you can create strings plus you can add one string to another and traverse over it with for loops

word1 = "Hello world!,"
word2 = "This is python"

print(word1 + " " + word2)

# with indexing you can access the characters of the string

word = "python"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])

# now with for loop 
for char in word:
    print(char)

for i in range(0, len(word)):
    print(word[i])


# slicing of strings basically 
# strings are immutable but we can access characters and make a new string

word = "python"
print(word[2:4])
sub_strings = word[2:5]
print(sub_strings)
sentence = "I am studying at ApnaCollege"
print(sentence[17:len(sentence)])
sub_strings2 = sentence[17:len(sentence)]
print(sub_strings2)

# you can also do negative indexing
word = "python"
print(word[-4:-2])
sub_strings = word[-4:-2]
print(sub_strings)
sentence = "I am studying at ApnaCollege"
print(sentence[-11:])
sub_strings2 = sentence[-11:]
print(sub_strings2)

# now we will talk about string formating
# how you can wring a string with different type
# with format function 
string = "Hello man, how are you {}".format("Jason")
print(string)

a = 10
b = 7
print("sum = :{}".format(a+b))
# multiple values
print("The sum of {} and {} is {}".format(a, b, a+b))

# format function with indexing
print("The sum is {2} of {1} and {0}".format(a, b, a+b))
# this is index formating and you just have to place correct index

# now we will se that we have fstring formating and is very easy
print(f"The sum and average of {a} and {b} is {a+b} and {(a+b)/2}")

# Now we will work on lists one of the four main data structures
# to create a list you just have to use square brackets 
list1 = [23, 45, 23, 67, 79]
print(list1)

list2 = [34, 56, 44, 67, 12]
print(list2)

list3 = [34, 345, 34, 57, 97, "Apna", "College", 56.67, 23.5]
# lets do slicing
print(f"The integer part of list is {list3[0:5]}")
print(f"The string part of list is {list3[5:7]}")
print(f"The float part of list is {list3[7:9]}")

# with negative indexing we do slicing
print(f"The integer part of list is {list3[-9:-4]}")
print(f"The string part of list is {list3[-4:-2]}")
print(f"The float part of list is {list3[-2:]}")

# so this is list and we use it for saving similar or dissimilar data together and it is mutable we can change the values after giving it new value

list4 = [12, 13, 14, 15, 16]
print(f"This is list4 {list4}")
list4[0] = "Hello!"
list4[1] = "How"
list4[2] = "are"
list4[3] = "you"
list4[4] = "?"
print(f"This is list4 after change {list4}")

# you can also check the type of list
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))

# now we will talk about some methods of lists

list5 = [12,23,345,243,223]
# to add a element here at the end of the list we can use append
print(list5)
list5.append(12345)
print(f"list5 after append {list5}")

# if you want to insert any element at any index of list than you need inser method
list6 = [45, 67, 23, 55, 83]
print(list6)
list6.insert(2, "How you doing?") # so here at the index second this text is inserted
# one can think that it is same as list6[2] = "How you doing?" but no, here with inset we do not change
# the value but sliding the right side values further and inserting the value at that index
# but with this one we do not add but replace the value
print(f"list6 after insert {list6}")

# next method sort
list7 = [45, 22, 7, 23, 13]
list7.sort()
print(f"list7 after sorting {list7}")
# this will sort it in increasing order but if you want it in reverse you can use
list7.sort(reverse=True)
print(f"list7 after revsered sorting {list7}")


# or you can revserse a string with reverse method
list8 = [45, 67, 23, 55, 39]
print(list8)
list8.reverse()
print(f"list8 after reversed {list8}")

# there are many more string methods
# now we see the use of for loop with list
# problem of finding index of a value by linear search
nums = [23, 45, 23, 56, 23]

val = 57
index = 0
val_found = False
for num in nums:
    if num == val:
        val_found = True
        break
    index += 1

if val_found:
    print(f"The number {val} is at index {index}")
else:
    print(f"The number {val} does not exist in this list.")



# Now we will work on tuple so tuples are same as list but they are immutable
# and can not be changed by trying to insert an element but you can create a new one.
tup = (12, 45, 32, 76, 81)
# tup[2] = 10 this is error
# we can do slicing
print(tup[1: 4])
# negative indexing
print(tup[-4: -1])

tup1 = (23, 45, 76, 32, 22, "Hello", "Python", 67.54, 87.23)
print(tup1)

# suppose you want to create a list with one element it is list
list9 = [3]
print(type(list9))

# but for tuple
tup2 = (6)
print(type(tup2)) # this is not type tuple, this is type int because of single int value
tup3 = ("Hi")
print(type(tup3)) # this is not type tuple, this is type string because of single string

# so if you want to create a tuple having single value
tup4 = (34,) # this comma will save you and you get your tuples created
print(type(tup4))

tup5 = ("Hi",)
print(type(tup5))
# both of these tup4 and tup5 are tuples type

# now we have some tuple methods
# first is index method which will get you index of the value
tup6 = (1, 3, 5, 6, 5, 6, 5, 2, 4)
index = tup6.index(6) # this will give you the index of first occurance
print(index)

# or if we want to count how many times an element is occured we can have count method
count = tup6.count(5)
print(count)

# adding elements of tuple 
sum = 0
for value in tup6:
    sum += value
print(f"The sum of elements {tup6} of tuple 6 is {sum}")


# Now we have dictionary, here we store data in a key value pair, this data structure is not 
# ordered, hence it is used to store related information together and we can 
# access the value only when you have key for it

dict1 = {
    "name": "Ashish",
    "cgpa": 8.48,
    "course": "MCA",
    8.48: "cgpa",
    28: "age"
}

print(dict1)
# and we can access values with keys
print(dict1["name"])
print(dict1["cgpa"])
print(dict1["course"])
print(dict1[8.48])
print(dict1[28])

# you can make any datatype your key
print(type(dict1))


# now we will see the dictionary methods where we will do some stuff
# first method is items() which give you both keys and values 
for key, value in dict1.items(): #this  how you can access key and value at the same time
    print(f"{key} : {value}")

print(dict1.items())

# you can also access keys only by keys() method
print(dict1.keys())
list_keys = list(dict1.keys())
print(list_keys)
for key in dict1.keys():
    print(f"this is key: {key}")

# you can also access values only by values() method
print(dict1.values())
list_values = list(dict1.values())
print(list_values)
for value in dict1.values():
    print(f"this is value : {value}")

# now for accessing values through keys you can use bracket notations but if that key does not 
# exist this will end up in an error and program will get stop
# which is not a good thing so we can use get method that helps us in getting value
# but gives us None type when no value found

# val = dict1["color"]
# print(val) this will get you error

val = dict1.get("name")
val2 = dict1.get("color")
print(val)
print(val2) # putput will be None

dict1['cgpa2'] = 9.2 # this is how you can add more pairs or
print(dict1)

dict1.update({
    "name2" : "Kumar",
    "cgpa3" : 8.7
}) # here you can add multiple pairs at once
print(dict1)
 # these 5 are dictionary methods

# now will study about sets which only honds unique value and are unordered having no indexes
# sets are mutable but elements of set are immutable
# it is unique so no duplication even if we try to do

set1 = {23, 56, 56, 56, 56, 56, 56, 56, 76, 43, 33}
print(set1) # only 5 values will print

# you can add element with add method but it must be unique
set1.add(56)
print(set1) # it will not add

set1.add(88) # this will add
print(set1)
set1.add(1)
print(set1)

# to create a empty set {} will not work
empty_set = {} # this will create a dictionary
print(type(empty_set))

empty_set = set() # calling constructor here
print(type(empty_set))

# next method is remove which will remove the element from set
set1.remove(56)
print(set1)

# next is pop which randomly removes any element form the set
print(set1.pop())
print(set1)

print(set1.pop())
print(set1)
print(set1.pop())
print(set1)

# next we have clear method which removes all element from set
set1.clear()
print(set1)

# next we have union method which gives us all elements combined in two different sets
set1 = {1, 4, 6, 5, 8}
set2 = {2, 4, 8, 3, 7}

set3 = set1.union(set2)
print(set3)

# next we have intersection which will gve you all common elements from both the sets
set4 = set1.intersection(set2)
print(set4)

# now we have a problem to solve, create list of tuples
student_data = [
    ("Ashish", "English"),
    ("Rinkesh", "Maths"),
    ("Rida", "Cloud"),
    ("Devraj", "English"),
    ("Aman", "Maths"),
    ("Vinay", "WebDev"),
    ("Bijuka", "pata nahi"),
    ("Bijuka", "Maths"),
    ("Aman","English"),
    ("Rida", "Hindi"),
    ("Devraj", "Punjabi"),
    ("Rinkesh", "pool"),
    ("Ashish", "coding")
]

# print all unique values of courses
courses_set = set()
for pair in student_data:
    courses_set.add(pair[1])
print(courses_set)

# or we can do a different method
courses_set = set()
for name, course in student_data:
    courses_set.add(course)
print(courses_set)

# you have to print name of students having courses Math and English
list_names = []
for name, course in student_data:
    if course == "English" or course == "Maths":
        list_names.append(name)

print(list_names)

# make a dictionary with names and courses
student_dict = {}

for name, course in student_data:
    if student_dict.get(name) == None:
        student_dict.update(
            {
                name: set()
            }
        )
        student_dict[name].add(course)
    else:
        student_dict[name].add(course)

print(student_dict)
for key, value in student_dict.items():
    print(key, value)

# this is the end of class 3 thank you