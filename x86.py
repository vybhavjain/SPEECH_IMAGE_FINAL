# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:05:13 2019

@author: VYBHAV JAIN
"""
import turtle
import fcomponent as fc
    
def trapezium(x):
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(60)
    turtle.forward(40)
    turtle.right(60)
    turtle.write(x)
    turtle.forward(40)
    
def system():
    turtle.penup()  
    turtle.setpos(-60,60) #coordinate is midpoint of base , so pass coordinates accordingly
    turtle.pendown()
    fc.rectangle1('                 1.CPU',300,240)  # passed breadth first then length
    turtle.penup()  
    turtle.setpos(-120,240)
    turtle.pendown()
    fc.rectangle1(' 2.Registers',60,30)
    
    
    turtle.penup()  
    turtle.setpos(-150,180)
    turtle.pendown()
    trapezium('ALU')
    
    #connecting Registers and ALU
    turtle.penup()  
    turtle.setpos(-120,240)
    turtle.pendown()
    turtle.right(210)
    turtle.right(90)
    fc.arrow()
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    fc.arrow()
    turtle.right(90)
    
    #Drawing control unit
    turtle.penup()  
    turtle.setpos(30,140)
    turtle.pendown()
    turtle.left(90)
    fc.rectangle1('Control unit',80,50)
    
    #connecting control unit and ALU
    turtle.penup()  
    turtle.setpos(-150,180)
    turtle.pendown()
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(30)
    fc.arrow()
    turtle.right(-90)
    turtle.forward(70)
    turtle.left(90)
    fc.arrow()
    turtle.right(90)
    
    
    turtle.penup()  
    turtle.setpos(-120,145)
    turtle.pendown()
    turtle.left(180)
    fc.arrow()
    turtle.right(180)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    fc.arrow()
    #turtle.right(90)
    
    ls = []
    turtle.penup()  
    ls = turtle.pos()
    turtle.setpos(ls[0],ls[1]-40) #coordinate is midpoint of base , so pass coordinates accordingly
    turtle.pendown()
    #turtle.left(90)
    fc.rectangle2('                 Input/Output devices',330,40)  # passed breadth first then length
    
    
    
    turtle.penup()  
    turtle.setpos(70,165)
    turtle.pendown()
    turtle.right(90)
    fc.arrow()
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    fc.arrow()
    turtle.right(90)
    
    turtle.penup()  
    turtle.forward(20)
    turtle.pendown()
    turtle.write('Main Memory')
    
    turtle.penup()  
    turtle.left(180)
    turtle.forward(20)
    turtle.pendown()
    
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(340)
    turtle.right(90)
    turtle.forward(100)    
    turtle.right(90)
    turtle.forward(190)
    
    turtle.done()

system()
