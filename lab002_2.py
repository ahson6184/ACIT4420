#creating an empty dictionary
student_grade=dict()

# number of elements as input
n = int (input("Enter number of elements:"))

#iterating til the range and getting value
for i in range(0,n):
    _key = input("Enter student name: " )
    _value = int(input("Enter student marks: "))
     # adding the elemnet 
    student_grade[_key]= _value
print(student_grade)
 
for x,y in student_grade.items():
    if y == 100:
      print( x, "has secrured highest possible grade")
        
    elif 90<y<100:
      print(x, "has secrured highest grade-A")
        
    else:
      print(x, "has failed the exam")
        
        