#CLASSES
class Dog:

    # Constructor: include two variables to pass in when creating a dog object
        def __init__(self,name,age):
              self.name = name
              self.age = age

    # Method
        def bark(self):     # self as argument of the method will point to the current object instance & must be specified when defining a method
            print("Woof!")  # When creating a method in a class always start with self

    #######################


# Objects
# Attributes and Methods
        
roger = Dog("Roger", 6) # will assign name and age

print(type(roger))      # will show roger is a dog
print(roger.age)        # will show age

roger.bark()     # will return "woof!"   --- allows object to call method

age = 8

print(age.bit_length)
print(age.imag)
print(age.real)

# objects allow access to various functions of specific object

items = [1, 2]

items.append(3)
items.pop()

    #######################

# INHERITANCE
class Pitbull(Dog):
        def grow(self):
            print("I'm aging!")

taz = Pitbull("Taz", 2)

taz.bark()       # will return 'woof!' --- Pitbull class has inherited methods from Dog class