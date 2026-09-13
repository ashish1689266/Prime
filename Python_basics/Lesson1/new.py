
    
students = {

'Aditya': 95,

'Shiva': 75,

'Kabir': 89,

'Rahul': 33,

'Aryan': 46

}

total_score = 0

for student in students:

    total_score = total_score + students[student]

print('The total score of all students is:', total_score)

average = total_score / len(students)

print('The average is', average)

top_scorer = 0

bottom_scorer = 100

for student in students:

    top_scorer = max(top_scorer, students[student])

    bottom_scorer = min(bottom_scorer, students[student])

print("The top scorer is:", top_scorer, "and the bottom scorer is:", bottom_scorer)

student_name = students.get(input('Which student do you want to find?'))

if student_name in students:

    print("Your student has been found")

else:

    print("Your student has not been found")

print("End of the program")