import turtle 
import fcomponent as fc

def start(r):               # Horizontal Oval
    turtle.penup()   
    turtle.setpos(0,60)
    turtle.pendown()
    turtle.penup()
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

    
def stop(r):               # Horizontal Oval
    turtle.penup()   
    turtle.setpos(-10,-220)
    turtle.pendown()  
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
    turtle.write("  Stop")

def flowchart1():

    start(25)   # function to print the start inside the oval

    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,20)
    turtle.pendown()

    fc.arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,0)
    turtle.pendown()
    fc.parallelogram("    Get a and b",40)
    turtle.setpos(0,-40)
    fc.arrow()
    fc.rhombus(60)   # draws a rhombus for the conditional statement 
    turtle.penup()   
    turtle.setpos(-30,-90)
    turtle.pendown()
    turtle.write('    is a>b?')
    
    
    # code if comparison is true 
    
    turtle.penup()   
    turtle.setpos(0,-40)
    turtle.pendown()
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(70)
    turtle.write('yes')  # results of comparison is true
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    fc.arrow()
    turtle.right(90)
    turtle.penup()   
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    fc.parallelogram("    display a ",30)
    turtle.right(90)
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(85) 
    turtle.left(180)

    turtle.right(90)
    fc.arrow()
    turtle.left(90)
    
    # code if comparison is flase
    
    turtle.penup()   
    turtle.setpos(0,-40)
    turtle.pendown()
    turtle.right(135)
    turtle.forward(60)
    turtle.right(45)
    turtle.forward(70)
    turtle.write('no') #results of comparison is false
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    fc.arrow()
    turtle.right(90)
    turtle.penup()   
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    fc.parallelogram("    display b ",30)
    turtle.right(90)
    turtle.forward(55)
    turtle.left(90)
    turtle.forward(100) 
    turtle.left(90)
    fc.arrow()
    turtle.right(90)
        
    stop(25)  # function to print inside oval stop
    turtle.hideturtle()
    turtle.done()

