# LISTS

dogs = ["doberman", "french bull", "pitbull", "golden retriever"]
otherStuff = ["Max", 32, True, "Tony", "Doc", False]    # can place multiple types in a list

print(dogs[2])  # return item in selected slot (pitbull)
print(dogs[1:3])    # returns items 1-2
print(dogs[-1]) # return item going from the backend of list (golden retriever)

print(len(otherStuff))  # returns length of (number of items in) list

# adding to and removing from lists

dogs.append("poodle")   # add items to list

dogs.extend(["pomeranian", "shitzuh"]) # adding items to list; can use to add another list to this list
otherStuff += ["15", 24, "Liz"]  # does the same as extends operator

otherStuff.remove("Tony")   # removes selected item
print(dogs.pop())  # moves and returns single item (the last item on the list)
print(dogs)     # shitzuh should no longer be on the list when this prints

items = ["Roger", 1, "Syd"]
print(items)
items.insert(2, "Test") # should include item (Test) at selected index (2)
print(items)

# sorting

dogs.sort() # sorts numerical or alphabetically; all items must be of the same type
dogs.sort(key=str.lower)    # ignoring capitalization
print(dogs)

names = ["Nya", "Zavhyn", "zara", "ayana", "Ashira"]
print(sorted(names, key=str.lower))     # sorts items, ignoring capitalization

# copy
otherStuffCopy = otherStuff[:]  # pulls all items ffrom respective list into new list (both list exist)

##############################

# TUPLES - cannot be modified (cannot add or remove)

names2 = ("James", "Auden", "Liana")

names2[0]    # returns item in index selected ("James")
names2.index("Auden")    # returns index where item is located (1)

len(names2)
print("Liana" in names2)    # returns boolean if item is located in tuple

newTuple = names2 + ("Charles", "Menyhara")  # creates new tuple using items from previous tuple and adds new items

##############################

# DICTIONARIES

pets = { "bird" : "Parrot", "cat" : "Sphinx", "dog" : "Sparki"}

print(pets["bird"])     # will return "Parrot"; can use single quotes as well
print(pets.get("cat"))  # returns "Sphinx"

pets.pop("cat")     # removes the cat item from the list

list(pets.keys())    # shows only the keys (bird and dog - cat was removed in line 63)
list(pets.values())  # shows only items in dictionary (parrot and sparki)

pets["rat"] = "Dino"    # adds key and item to dictionary

del pets['rat']     # deletes slected key and item

#############################

# SETS - not ordered and immutable

friends = {"Justic", "Caleb", "Justin"}
moreFriends = {"Quentin", "Jayce", "Caleb"}
moreFriends2 = {"Liana", "Dom", "Koi"}

intersect = friends & moreFriends   # finds intersection (Caleb)
print(intersect)    # prints the intersect (Caleb)
modify = friends - moreFriends  # removes common items (Caleb)
print(modify)   # returns only items that are not common

mod = friends | moreFriends2     # gets every item of both sets
print(mod)  # presents all items