# Functions allow running a set of instructions when called

# Promotes readability and code reuse
# Starts with function name
# Body of function is the set of instructions
# Function name should be descriptive so other know what it doess

def hello():
    print('Hello World!')


# Call the function
    
hello()

###

# creating function that will pass an argument when calling

def hello(name):
    print('Hey there ' + name)

hello("Nyasha")     # this will input the selected value into the name argument and pass as 'Hey there Nyasha'
hello('Max')        # 'Hey there Max'

# Parameters v Arguments
# parameters: values accepted by the function inside the function definition
# arguments: values passed to the function when we call it

###

# arguments can have default values if it is not specified

def hey(name = "my friend"):
    print("Hello " + name)

# ^^^ will return 'my friend' if argument is not inputted when calling. This prevents errors from happening
    
hey()

###

def welcomeFriendAndAge(name, age):
    print("Hey " + name + ", you are " + str(age) + " years old.")

welcomeFriendAndAge('Erin', 55)

###

# Return Statements
def helloThere(person):
    if not name:
        return
    print("There you are " + person + "!")

# if there is no argument inputted, nothing is returned (can help avoid exxceptions/errors). If something is inputted, it will return print statement and name selected
    
###
    
# Global v Local variables
# when a variable is set inside a function it is local and cannot be called outside the function
# if a variable is set outside and before the function, it is global and can be called by functions created afterwards
    
###

# Nested functions: hide functionality inside function if not useful elsewhere

def talk(phrase):
    def say(word):
        print(word)

        words = phrase.split(' ')
        for word in words:
            say (word)

talk('I am going to buy the milk')

# nonlocal
def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()

# closures : if you return nested function from a function, nested function has access to the variables defined in the function even if that function is not active anymore
def counter():
    count = 1

    def incrementation():
        nonlocal count
        count = count + 2
        return count
    
    return incrementation

increment = counter()

print(increment())  # 3
print(increment())  # 5