# how to make a list
favMovies = ["Fury", "Saving Private Ryan", "T-34"]
# print the whole list 
print(favMovies)
# print individuals
print(favMovies[0])
# to add to the list you can use append or insert
# append adds to the end
favMovies.append("Full Metal Jacket")
print(favMovies)
# insert will put the item wherever you want it 
favMovies.insert(1, "Band of Brothers")
print(favMovies)
# how to remove items from list
# remove by name or by index
# remove by name use "remove"
favMovies.remove("Fury")
print(favMovies)
#favMovies.remove("Endgame") item must be in list to be removed
# pop will remove last item unless an index is given
favMovies.pop()
print(favMovies)
favMovies.pop(1) # will remove what ever is in index
print(favMovies)

# get the length of a list
# this is a function 
# function name is "len"
print("My list has " + str(len(favMovies)) + " items")
favMovie = input("what is your favorite movie? ")
favMovies.append(favMovie)
print(favMovies)
print(favMovies[len(favMovies) - 1])

# loop through a list
count = 1 

for movie in favMovies:
	print("My number " + str(count) + " movie is " + movie)
	count = count + 1 

numList = [1, 8, 27, 44, 52, 69]
# challenge: move through the list and add all the numbers together then print the sum

total = 0

for number in numList:
	total = total + number

print("the sum is " + str(total))

if "T-34" in favMovies:
	favMovies.remove("T-34")
	print("T-34 was removed from the list")
else:
	print("not in list")

# how to turn string to list
myString = "arizona"
myList = list(myString)
print(myList)

# how to create a list where underscores replace the letters
guessList = []
for a in myList:
	guessList.append("_")
print(guessList)

# how to replace specific item in list
# so say the user types r for guess you would 
guessList[1] = "r"
print(guessList)

choice = input("Type a word:")
if choice == myWord:
	print("its a match")
else:
	print("not a match")