# -*- coding: utf-8 -*-
import turtle
import math 

    
def circle(radius):    
        turtle.up()
        turtle.goto(0,radius)
        turtle.down()    
        turtle.color("red")
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
            return  

def square1(length,color):
    n = 4
    x = color
    #z = color1 # this refers to the color that is filled in the middle
    turtle.color('red',x)
    turtle.begin_fill()
    edges = n
    length1 = length
    angle = 360.0 / edges
    for i in range(n):
        turtle.forward(length1)
        turtle.right(angle)
    turtle.end_fill()
    turtle.done()

def rectangle1(dim):
        turtle.forward(dim)
        turtle.left(90)
        turtle.forward(dim/2)
        turtle.left(90)
        turtle.forward(dim)
        turtle.left(90)
        turtle.forward(dim/2)
        turtle.left(90)
