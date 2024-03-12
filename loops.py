# While Loops

count = 0

while count < 10 :
    print("Keep going...")
    count += 1

print("Alright, let's go home")

#############

# For Loops

items = [1, 2, 3, 4]

for i in items:
    print(i)

for index, i in enumerate(items):
    print(index, i)

for thing in range(15):
    print(thing)

##############

# Continue
    
chest = [5, 6, 7, 8]

for j in chest:
    if i == 7:      # will not print 7 because it is true. Continue will tell it to skip that (5, 6 and 8 will be printed)
        continue
    print(j)

# Break

for j in chest:
    if i == 7:
        break       # this will stop the loop entirely (only 5 and 6 will be printed)
    print(j)