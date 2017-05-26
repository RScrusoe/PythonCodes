
import turtle               # allows us to use the turtles library
import time
wn = turtle.Screen()        # creates a graphics window
t = turtle.Turtle()

def tree(n,bl):
    
    if n>0:
            
        t.forward(bl)
        t.right(30)
        tree(n-1,bl-5)
        t.left(60)
        tree(n-1,bl-5)
        t.right(30)
        t.backward(bl)
        
branchLen = 75
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
tree(6,branchLen)
time.sleep(5)

