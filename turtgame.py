from turtle import *

Fuze = Turtle()
myScreen = Fuze.getscreen()
Fuze.penup()
Fuze.goto(myScreen.window_width() / 2 - 200, myScreen.window_width()/2-50)
Fuze.hideturtle()
score = 0

def updateScore():
	Fuze.clear()
	Fuze.write("Score: " + str(score), False, "left", font=("Arial", 20, "normal"))

updateScore()









screen.mainloop()