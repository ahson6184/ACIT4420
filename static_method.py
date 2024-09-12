'''
A static method does not take the self or cls (short for class) references as a parameter 
because no instance is involved in it. It takes only arguments. If you add self parameter, 
it would be an instance method, not a static method. Similarly, if you use cls parameter, 
it would be a class method, not a static method.


class Student:
    @staticmethod
    def display():
        print("I am student.")

# Ouside the class definition.
# Call the static method using the name of class.
Student.display()

# We can also call the static method by creating an instamce of class.
obj = Student()
obj.display()


class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

# Outside the class definition.
# We can access and call static methods on the class itself, without creating an instance of the class.
result1 = MathOperations.add(5, 3)
result2 = MathOperations.subtract(10, 4)
result3 = MathOperations.multiply(6, 2)
result4 = MathOperations.divide(8, 2)

# Displaying the results.
print("Addition:", result1)
print("Subtraction:", result2)
print("Multiplication:", result3)
print("Division:", result4)


# Python program to use the class variable inside a static method.
class MyClass:
    class_var = "I am a class variable"

    @staticmethod
    def static_method():
      # Calling a class variable using class name inside a static method.
        print(MyClass.class_var) 

# Calling the static method through the class
MyClass.static_method()



# Python program to use the instance variable inside a static method.
class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method(instance):
        print(instance.instance_variable)

# Creating an instance of MyClass.
obj = MyClass("I am an instance variable")

# Calling the static method by passing an instance to the static method.
MyClass.static_method(obj)


# Python program to use the class method inside a static method.
class MyClass:
    class_var = "I am a class variable"

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print(f"Accessing class variable: {cls.class_var}")

    @staticmethod
    def static_method():
        print("This is a static method")
        MyClass.class_method()  # Calling the class method

# Call the static method
MyClass.static_method()
'''

# Python program to use an instance method inside a static method.
class MyClass:
    def instance_method(self):
        print("This is an instance method")

    @staticmethod
    def static_method():
        print("This is a static method")
        instance = MyClass()  # Create an instance of the class
        instance.instance_method()  # Call the instance method

# Call the static method
MyClass.static_method()