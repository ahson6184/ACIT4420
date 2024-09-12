"""
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Noah","Emma","Ashirah")


# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def ur_function(**kids):
  print("Her last name is " + kids["lname"])

ur_function(fnamae="Ashirah",lname="Sonar")
  
# Default parameter value
def my_country(country="Norway"):
    print("I am from " + country)

my_country("Sweden")
my_country("Bangladesh")
my_country()
my_country("Indoneshia")

# List as a argument
def my_fruits(fruits):
    for fruit in fruits:
        print(fruit)
fav_fruits= ['mango','banana','pineapple']
my_fruits(fav_fruits)


# return statement in function
def my_return(x):
  return 5*x

print(my_return(10))
print(my_return(100))
print(my_return(9.5))



# pass statement
def myfunction():
    pass

#Positional-only argument(wokrs python3.8 or later version)
def my_function(x, /):
    print(x**2)
my_function(3)



def tri_recusrsion(k):
    if(k>0):
        result= k + tri_recusrsion(k-1)
        print(result)
    else:
        result=0
    return result
print("\n\nRecursion Exam Results")
tri_recusrsion(4)
"""
#labquiz 5.September
def append_to_list(value,my_list=[]):
    my_list.append(value)
    return my_list
print(append_to_list(1))
print(append_to_list(2))  
print(append_to_list(3))
print(append_to_list(4,[]))

