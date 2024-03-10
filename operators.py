from enum import Enum

# Bitwise Operators : not common, but helpful to know

# &     performs binary AND
# |     performs binary OR
# ^     performs binary XOR
# ~     performs binary NOT operation
# <<    shift left
# >>    shift right

########################################

# Ternary Operator

def is_adult(age):
    return True if age >= 18 else False


#######################################

# String Methods

name = "Erin"
print("max".upper()) # will make all letters uppercase - can use .lower()
print("max left".title()) # will capitalize each word
print("MAX".islower()) # will check is letters are lowercase (returns a boolean)
print(len(name)) # prints number of characters in variable's value

# splicing
sister = "Ebony"
print(sister[1]) # prints character in place of that number ("b")
print(sister[2:4]) #prints characters starting at first number to last ("ony")

# OTHERS
# startswith()
# endswith()

######################################

# Enums : often used for constants to prevent people from using; cannot be reassigneds

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value) # will print value of called variable within class

######################################

# types
name = "Max"
age = 39

print(type(name))       # this should print the data type of 'name' in the console (should come out as string)

print(type(name) == str)        # this checks if data type equals string, and puts out a boolean (True or False)
print(isinstance(age, int))     # does the same, checking datatype matches (is age an integer)

######################################

# conversion
myAge = int("20")

price = "3.76"
thePrice = float(price)     # called 'casting'

# complex   for complex numbers
# bool  for booleans
# list  for lists
# tuple for tuples
# range     for ranges
# dict  for dictionaries
# set   for sets

# Arithmetic Operators : + , - , * , / , % , ** , //