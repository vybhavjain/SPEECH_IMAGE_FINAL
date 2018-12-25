import turtle
import math

def circle(radius,color,color1):   
    x = color
    y = color1
    turtle.up()
    # go to (0, radius)
    turtle.goto(0,radius)
    turtle.down()    
    turtle.color(x,y)
    turtle.begin_fill()
    # number of times the y axis has been crossed
    times_crossed_y = 0
    x_sign = 1.0
    while times_crossed_y <= 1:
        # move by 1/360 circumference
        turtle.forward(2*math.pi*radius/360.0)
        # rotate by one degree (there will be
        # approx. 360 such rotations)
        turtle.right(1.0)
        # we use the copysign function to get the sign
        # of turtle's x coordinate
        x_sign_new = math.copysign(1, turtle.xcor())        
        if(x_sign_new != x_sign):
            times_crossed_y += 1
        x_sign = x_sign_new
    turtle.end_fill()
    return  

def rectangle1(dim1,dim2,color,color1):
    x = color
    z = color1 # this refers to the color that is filled in the middle
    turtle.color(x,z)
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(dim1)
        turtle.left(90)
        turtle.forward(dim2)
        turtle.left(90)
    turtle.end_fill()
    return    
    
def star(color,color1,radius):
    x = color
    z = color1 # this refers to the color that is filled in the middle
    turtle.color(x,z)
    #color(x,z)
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()

    
def design(x):   
    turtle.color(x)
    for i in range(50):
        turtle.forward(100)
        turtle.left(123)
    turtle.done()

   
def polygon(n,length,color,color1):
    x = color
    z = color1 # this refers to the color that is filled in the middle
    turtle.color(x,z)
    turtle.begin_fill()
    edges = n
    length1 = length
    angle = 360.0 / edges
    for i in range(n):
        turtle.forward(length1)
        turtle.right(angle)
    turtle.end_fill()
    turtle.done()
    


'''
def starcircle(color,color1,radius):  # needs to be worked on and checked
    x = color
    z = color1 # this refers to the color that is filled in the middle
    turtle.color(x,z)
    #color(x,z)
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    myTurtle = turtle.Turtle()
    turtle.goto(5,radius)
    #turtle.right(90)
    #turtle.forward(100)
    #turtle.right(90)
    #turtle.forward(100)
    myTurtle.circle(100)
    ##normalcircle(100,y)
    turtle.done()
starcircle('red','black',5)
'''
"""
y = 'blue'    # color to be passed 
a = 'red'
#triangle(y,a)   
#square1 (100,a,y)
#rectangle1(100,30,a,y)    
#circle(50,y,a)
star(y,a,40)
"""
print('finished')


