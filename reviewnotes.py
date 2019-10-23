# Jarrett Thomas
# Period 4
# Oct 14th, 2019

# variable declaration and assignment
# Examples
myNum = 12 # interger type
myString = "12" # string type 
myNum + 3 # ok 
myString + "3" #  ok

# make a variable and assign it to the value of your favorite movie
# print "my favorite movie is" followed by the variable 

myMov = "Saving Private Ryan"
print("My favorite movie is " + myMov )

# while loops 
# example - print from 1 to 10 
x = 1
while x <= 10:
	print(x)
	x = x + 1 


# count down from 100 using a while loop
x = 100
while x >= 0:
	print(x)
	x = x - 1 

# string concatenation 
# means putting 2 strings together 
# example
myName = "Jarrett"
print("Hello " + myName)

# input
# example
yourName = input("What is your name? ")
print("Hello " + yourName + " have a nice day")
# number = input("please type in a number: ") 
# number = int(number) + 10 
# print("The number is " + str(number))


# ask for two numbers, add them, and print the sum 
Num1 = input("Please type a number: ")
Num2 = input("Please type another number: ")
newNum = int(Num1) + int(Num2)
print("The new number is " + str(newNum))

# if / else statements
# example
num = int(input("enter a number: "))
if num > 100:
	print("that number is more then 100")
elif num == 100:
	print("your number is equal to 100")
else:
	print("your number is less then 100")

# ask if today is your birthday 
# if yes print happy birthday 

bDay = input ("Is today your birthday? y/n: ")
if bDay == "y":
	print("happy birthday")
elif bDay == "no":
	print("have a good day regardless")
else:
	print("your answer does not make sense")