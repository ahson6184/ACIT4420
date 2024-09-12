class Shark:
    #class variables
    animal_type = "fish"
    location = "ocean"
    followers = 5
    def __init__(self, name, age):
        self.name = name
        self.age = age
'''
new_shark = Shark()

print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)

new_shark = Shark("Same",5)
stevie = Shark("Stevie",8)
print(new_shark.name)
print(new_shark.age)

print(stevie.name)
print(stevie.age)
'''
class Shark:

    # Class variables
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")


def main():
    # First object, set up instance variables of constructor method
    sammy = Shark("Sammy", 5)

    # Print out instance variable name
    print(sammy.name)

    # Print out class variable location
    print(sammy.location)

    # Second object
    stevie = Shark("Stevie", 8)

    # Print out instance variable name
    print(stevie.name)

    # Use set_followers method and pass followers instance variable
    stevie.set_followers(77)

    # Print out class variable animal_type
    print(stevie.animal_type)

if __name__ == "__main__":
    main()