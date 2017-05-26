
import turtle               # allows us to use the turtles library
import time
wn = turtle.Screen()        # creates a graphics window
t = turtle.Turtle()
t.color("green")
n=1
tm=10
for i in range(200):
	t.right(tm)
	tm-=0.03
	t.forward(n)
	n+=0.1



time.sleep(2)

