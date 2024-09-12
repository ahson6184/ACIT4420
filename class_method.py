'''
class MyClass:
    @classmethod
    def my_class_method(cls):
        print("I am class method in Python")

# Outside the class definition.
# Accessing and calling class method using the name of class.
MyClass.my_class_method()

#Class Method with Parameters
class MyClass:
    @classmethod
    def greet(cls, name):
        return f"Hello, {name}!"

# Outside the class definition.
message = MyClass.greet("Alice")
print(message)



class MyClass:
    @classmethod
    def sum(cls, x, y):
      # Perform addition operation with the parameters.
        result = x + y
        return result

# Outside the class definition.
# Call the class method with parameters
result = MyClass.sum(10, 20)

# Print the result.
print("Result:", result)


class MyClass:
    class_variable = 0  # This is a class-level variable.

    @classmethod
    def increment(cls):
        cls.class_variable += 1 # Accessing class variable inside the class method.

# Outside the class definition.
# Access the class variable using the class name.
print("Class Variable (Before Increment):", MyClass.class_variable)

# Call the class method to increment the class variable.
MyClass.increment()

# Access the class variable again after incrementing.
print("Class Variable (After Increment):", MyClass.class_variable) 


# Accessing instance variable from class method using instance parameter
class Student:
  # Constructor definition.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def student_info(cls, self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")

# Create instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Call the class method with different instances
Student.student_info(student1)
Student.student_info(student2)


#Accessing instance variable in in class method using class method ?!

class Employee:
  # Constructor definition.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def employee_info(cls, name, salary):
        instance = cls(name, salary) # Here, instance variable represents self.
        print(f"Employee Name: {instance.name}")
        print(f"Employee Salary: {instance.salary}")

# Call the class method using class name and pass instance data.
Employee.employee_info("John", 50000)
Employee.employee_info("Emily", 60000)

#Always remember that if you want to access instance variables within a class method, you should either pass an object as a 
#parameter to the class method definition or create an object within the class method

class MyClass:
    def instance_method(self):
        print("This is an instance method.")

    @classmethod
    def class_method(cls):
        print("This is a class method.")

      # Create an instance of the class.
        instance = cls() # cls refers to the class itself.
      # Above statement is same as the below statement.
      # instance = MyClass()
        

      # Call the instance method on the created instance
        instance.instance_method()

# Call the class method to invoke the instance method
MyClass.class_method()
'''

class MyClass:
    def instance_method(self):
        print("This is an instance method.")

    @classmethod
    def class_method(cls, self): # Here, instance refers to the current instance of class. 
        print("This is a class method.")

      # Call the instance method on the provided instance
        self.instance_method()


# Create an instance of the class
my_instance = MyClass()

# Call the class method and pass the instance as an argument
MyClass.class_method(my_instance)