import turtle 
import fcomponent as fc

def start(r):               # Horizontal Oval
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,120)
    turtle.pendown()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-(r/1.414),120+(r/1.414))
    turtle.pendown()
    turtle.write("  Start")
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
    turtle.circle(r,45)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)

def flatoval1(r):               # Horizontal Oval
    turtle.right(45)
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-(r/1.414),-(210+(r/1.414)))
    turtle.pendown()

    #turtle.write("Start")
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)

def stop():
   turtle.penup()   
   turtle.setpos(0,-180)
   turtle.pendown()   
   flatoval1(25)
   turtle.write("  Stop")
               
   
def flowchart1():

    start(25)   # function to print the start inside the oval

    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,90)
    turtle.pendown()

    fc.arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,70)
    turtle.pendown()
    fc.rectangle("  Initialise sum = 0 ",50)
    turtle.setpos(0,40)
    fc.arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,20)
    turtle.pendown()
    fc.parallelogram('  get a' ,20)
    turtle.setpos(0,-20)
    fc.arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,-40)
    turtle.pendown()
    fc.rectangle("  sum = sum + a ",50)
    turtle.setpos(0,-70)
    fc.arrow()

    fc.rhombus(70)  # position here is 0,-70
    
    # loop back starts here
    
    turtle.right(90)
    turtle.forward(70)
    turtle.right(45)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward((100+(70/1.414)))
    turtle.write('yes')
    turtle.right(90)
    turtle.forward(50+(70/1.414))
    turtle.left(90)
    fc.arrow()
    turtle.right(90)

    # loopback is over
   
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-25,-110)
    turtle.pendown()
    turtle.write('Any more')
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-35,-125)
    turtle.pendown()
    turtle.write('numbers left to')
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-25,-140)
    turtle.pendown()
    turtle.write('     Add?')
    
    # end of rhombus condition
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,-70)
    turtle.pendown()
    
    # switch to new location with required arrow
    
    turtle.right(45)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(45)
    turtle.forward(25)
    turtle.write('  No')
    turtle.forward(10)
    turtle.left(90)
    fc.arrow()
    
    
    stop()  # function to print inside oval stop
    turtle.hideturtle()
    turtle.done()

#flowchart1()
