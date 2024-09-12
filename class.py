"""
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
"""
class MyClass:    
# Constructor declaration.
    def __init__(self):
        self.x = 20 # Instance variable
        self.y = 40 # Instance variable

  # Instance method definition.
    def m1(self):
      # Accessing instance variables inside an instance method.
        print("Value of x = ", self.x)
        print("Value of y = ", self.y)

# Outside class definition.
# Create an object of class MyClass.
obj = MyClass()

# Accessing instance method using object reference variable obj.
obj.m1()

# https://www.scientecheasy.com/2023/09/instance-method-in-python.html/