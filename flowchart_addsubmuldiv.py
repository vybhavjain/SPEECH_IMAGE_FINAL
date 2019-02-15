import turtle 
import fcomponent as fc


def start(r):               # Horizontal Oval
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-(r/1.414),60+(r/1.414))
    turtle.pendown()
    turtle.write("  Start")
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
    turtle.circle(r,45)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)

        
def flatoval1(r):               # Horizontal Oval
    turtle.right(45)
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-(r/1.414),-(162.5+(r/1.414)))
    turtle.pendown()
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)    

def stop():
   turtle.setpos(0,-155)
   fc.arrow()
   turtle.penup()   
   turtle.setpos(0,-180)
   turtle.pendown()   
   flatoval1(25)
   turtle.write("  Stop")
         
def flowchart(x):

    start(25)   # function to print the start inside the oval
   # turtle.left(45)
    turtle.setpos(0,20)
    fc.arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,0)
    turtle.pendown()
    fc.parallelogram("     Get a and b",40)
    turtle.setpos(0,-40)
    fc.arrow()    
    turtle.penup()   
    turtle.setpos(0,-60)
    turtle.pendown()

    y = '  ' + x + " a and b "
    
    fc.rectangle(y,45)
    turtle.setpos(0,-100)
    fc.arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,-120)
    turtle.pendown()
    fc.parallelogram("    Display the result",50)

    stop()  # function to print inside oval stop
    turtle.hideturtle() # function to remove turtle cursor.
    turtle.done()
