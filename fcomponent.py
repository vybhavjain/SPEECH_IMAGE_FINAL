# File containing all the standard elements of a flowchart
import turtle 

def arrow():
    turtle.left(135)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.right(45)
    turtle.right(180)

def rectangle(x,y): 
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(2*y)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.write(x)
    turtle.forward(y)
    
def rectangle1(x,y,z):  # for structure 
    turtle.forward(y/2)
    turtle.left(90)
    turtle.forward(z)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(z)
    turtle.left(90)
    turtle.write(x)
    turtle.forward(y/2)

def rectangle2(x,y,z):  # for I/O
    turtle.forward(2*y/3)
    turtle.left(90)
    turtle.forward(z)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(z)
    turtle.left(90)
    turtle.write(x)
    turtle.forward(y/3)
    
def parallelogram(x,y): 
    turtle.forward(y+5)
    turtle.left(70)
    turtle.forward(20)
    turtle.left(110)
    turtle.forward(2*y)
    turtle.left(70)
    turtle.forward(20)
    turtle.left(110)
    turtle.write(x)
    turtle.forward(y-5)
    
def rhombus(x):
    turtle.right(45)
    for i in range(4):
        turtle.forward(x)
        turtle.right(90)

  