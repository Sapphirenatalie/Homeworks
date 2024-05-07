grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list1=list(grades[0])
print('Grades of Aaron:', list1)
grade_1=(sum(list1)/len(list1))
print('Average grade of Aaron:', grade_1)

list2=list(grades[1])
print('Grades of Bilbo:', list2)
grade_2=(sum(list2)/len(list2))
print('Average grade of Bilbo:', grade_2)

list3=list(grades[2])
print('Grades of Johnny:', list3)
grade_3=(sum(list3)/len(list3))
print('Average grade of Johnny:', grade_3)

list4=list(grades[3])
print('Grades of Khendrik:', list4)
grade_4='%.2f'% (sum(list4)/len(list4))
print('Average grade of Khendrik:', grade_4)

list5=list(grades[4])
print('Grades of Steve:', list5)
grade_5=(sum(list5)/len(list5))
print('Average grade of Steve:', grade_5)


list_of_average_grades=[grade_1, grade_2, grade_3, grade_4, grade_5]
print('List of average grades:', list_of_average_grades)

list_of_students=list (students)
print('List of Students:', list_of_students)
list_of_students.sort()
list_of_students_abc=sorted(list_of_students)
print('List of students by alphabet:', list_of_students_abc)

grades_of_students=dict(zip(list_of_students_abc, list_of_average_grades))
print('Dictionary:', grades_of_students)


