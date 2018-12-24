# -*- coding: utf-8 -*-

import turtle 

def flatoval(r):               # Horizontal Oval
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

    
def flatoval1(r):               # Horizontal Oval
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)

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

def start():
    turtle.penup()   
    turtle.setpos(0,60)
    turtle.pendown()
    #turtle.write("Start")
    flatoval(25)

def stop():
   turtle.penup()   
   turtle.setpos(-10,-220)
   turtle.pendown()   
   flatoval1(25)
   turtle.write("  Stop")

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
    turtle.penup()   
    turtle.setpos(-30,-90)
    turtle.pendown()
    turtle.write('    is a>b?')
    
    
def flowchart1():

    start()   # function to print the start inside the oval

    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,20)
    turtle.pendown()

    arrow()
    #turtle.left(90)
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,0)
    turtle.pendown()
    parallelogram("    Get a and b",40)
    turtle.setpos(0,-40)
    #turtle.right(90)
    arrow()
    #turtle.left(90)
    rhombus(60)   # draws a rhombus for the conditional statement 
    
    # code if comparison is true 
    
    turtle.penup()   
    turtle.setpos(0,-40)
    turtle.pendown()
    turtle.forward(60)
    #turtle.right(90) 
    turtle.left(45)
    turtle.forward(70)
    turtle.write('yes')  # results of comparison is true
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    arrow()
    turtle.right(90)
    turtle.penup()   
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    parallelogram("    display a ",30)
    turtle.right(90)
    turtle.forward(55)
    turtle.right(90)
    #turtle.setpos(0,-220)
    turtle.forward(85) 
    turtle.left(180)

    turtle.right(90)
    arrow()
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
    arrow()
    turtle.right(90)
    turtle.penup()   
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    parallelogram("    display b ",30)
    turtle.right(90)
    turtle.forward(55)
    turtle.left(90)
    #turtle.setpos(0,-220)
    turtle.forward(100) 
    turtle.left(90)
    arrow()
    turtle.right(90)
        
    stop()  # function to print inside oval stop
    turtle.hideturtle()
    turtle.done()

flowchart1()

