'''
#create a class wth property x
class myclass:
    x=5

#define an objct
p1=myclass()
print(p1.x)

# __init__() function

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #The __str__() function controls what should be returned when the class object is represented as a string.    
    def __str__(self):
        return f"{self.name}({self.age})"
    def myfunc(self):
        print("My name is",self.name)
p1= person("John",56)
p1.age=40
#del p1.age
print (p1.name)
print(p1.age)
print (p1)
p1.myfunc()



class MyClass:
    shared_list=[]    
    def __init__(self,val):
        self.instance_list=[]
        self.instance_list.append(val)
        self.shared_list.append(val)
obj1=MyClass(1)
obj2=MyClass(2)
obj3=MyClass(3)

print(obj1.shared_list)
print(obj2.shared_list)
print(obj3.shared_list)

print(obj1.instance_list)
print(obj2.instance_list)
print(obj3.instance_list)



class MyClass:
    def method(self):
        return 'instance method called'
    @classmethod
    def classmethod(cls):
        return 'Class method called',cls
    @staticmethod
    def staticmethod():
        return 'static method called'

class MyClass:
  # Instance method definition.
    def ins_method(self):
        print("I am an instance method")

# Outside class definition.
# Create an object of class MyClass.
obj = MyClass()

# Accessing instance method using object reference variable obj.
obj.ins_method()

class MyClass:
    x = 20 # class variable
    y = 30 # class variable

  # Instance method definition.
    def m1(self):
      # Accessing class variables using class name inside instance method.
        print("Value of x = ", MyClass.x)
        print("Value of y = ", MyClass.y)

# Outside class definition.
# Create an object of class MyClass.
obj = MyClass()

# Accessing instance method using object reference variable obj.
obj.m1()


class MyClass:
    def m1(self):
        print("I am m1 method")
    
    def m2(self):
      # Calling an instance method from inside another instance method.
        self.m1()
        print("I am m2 method")


# Outside class definition.
# Create an object of class MyClass.
obj = MyClass()
# Accessing instance method using object reference variable obj.
obj.m2()

class Calculator:
  # Declare instance methods for addition, subtraction, multiplication, and division.
    def sum(self, x, y):
        z = x + y # Local variable.
        print("Addition: ", z)
    
    def sub(self, x, y):
        z = x - y
        print("Subtraction: ", z)
    
    def prod(self, x, y):
        z = x * y
        print("Multiplication: ", z)
    
    def div(self, x, y):
        z = x / y
        print("Division:  ", z)

c1=Calculator()
c1.sum(100,200)
c1.prod(10,10)
c1.sub(20,30)
c1.div(1000,5)



# https://www.scientecheasy.com/2023/09/instance-method-in-python.html/


class calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sum(self):
        z= self.x+self.y
        return z
    def sub(self):
        z= self.x-self.y
        return z
    def prod(self):
        z=self.x*self.y
        return z
    def div(self):
        z= self.x/self.y
        return z

#Outside the call definition
c=calculator(60,120)

print(c.sum())
print(c.sub())
print(c.prod())
print(c.div())


#Advanced example
class MyClass:    
    x = 20 #class variable"
    def __init__(self):
        self.x = 30 #instance variable
    def m1(self):
        print(self.x) #Accessing instance variable
        print(MyClass.x) # Accessing class variable
    
    #creating an instance of My class
    
c = MyClass()
    
c.m1()

  

class MyClass:
    x = 20 # class variable
    def __init__(self):
        self.x = 30 # instance variable

    def m1(self):
        print(self.x) # Accessing instance variable.
        print(MyClass.x) # Accessing class variable.

# Creating an instance of class MyClass.
c = MyClass()
c.m1()
'''

# Example of class variable, instance variable and local variable

class MyClass:
    x = 20 #Class variable
    def __init__(self):
        self.x = 30 #instance variable
    
    def m1(self):
        x = 40 #local variable
        print(x)
    
    def m2(self):
        print(self.x)
        print(MyClass.x)
        self.m1()

#Creaying instance of my class
c=MyClass()
c.m2()    
        