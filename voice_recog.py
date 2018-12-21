# -*- coding: utf-8 -*-
import turtle
import speech_recognition as sr
import re
import shapes
from flowchart_addsubmuldiv import flowchart
#import comparator
import color_shape

def findmatches(pattern, phrase):

    for p in patterns:
        match= re.findall(p, phrase)
        return match


r = sr.Recognizer()
with sr.Microphone() as source:
    print('Say Something')
    audio=r.listen(source)
    
try:
    print('Google thinks you said:\n' + r.recognize_google(audio))
    
except:
    pass

n=r.recognize_google(audio)
patterns= [r'\d+']
radd=findmatches(patterns, n)

if len(radd)==0:
    int22=int('1')
else:
    str1 = ''.join(radd)
    int22 = int(str1)
    
wordList = re.sub("[^\w]", " ",  n).split()



if 'circle' in wordList:
    #if 'color' in wordList:
    if "red" in wordList:
        x = 'red'
    elif "blue" in wordList:
        x = 'blue'    
    elif "orange" in wordList:
        x = 'orange'    
    elif "yellow" in wordList:
        x = 'yellow'    
    elif "black" in wordList:
        x = 'black'    
    elif "violet" in wordList:
        x = 'violet'        
    else:
        x = 'black'
    color_shape.circle(20*int22,'white',x)
    turtle.hideturtle()
    turtle.done()

elif 'square' in wordList:
    if "red" in wordList:
        x = 'red'
    elif "blue" in wordList:
        x = 'blue'    
    elif "orange" in wordList:
        x = 'orange'    
    elif "yellow" in wordList:
        x = 'yellow'    
    elif "black" in wordList:
        x = 'black'    
    elif "violet" in wordList:
        x = 'violet'        
    else:
        x = 'black'
    shapes.square1(20*int22,x)
    print('finished')
    turtle.done()
    
elif 'rectangle' in wordList:
    if "red" in wordList:
        x = 'red'
    elif "blue" in wordList:
        x = 'blue'    
    elif "orange" in wordList:
        x = 'orange'    
    elif "yellow" in wordList:
        x = 'yellow'    
    elif "black" in wordList:
        x = 'black'    
    elif "violet" in wordList:
        x = 'violet'        
    else:
        x = 'black'
        
    color_shape.rectangle1(20*int22,(20*int22)/2,"black",x)
    turtle.done()
    
elif 'flowchart' in wordList:
    if 'add' in wordList:
        flowchart('add')
    elif 'subtract' in wordList:
        flowchart('subtract')
    elif 'multiply' in wordList:
        flowchart('multiply')
    elif 'division' in wordList:
        flowchart('division')
    else:
        import comparator
        comparator.flowchart1()
        print("OK")
        
elif 'look' in wordList:
    import loopback
    loopback.flowchart1()        
        
elif 'star' in wordList:
     #if 'color' in wordList:
    if "red" in wordList:
        x = 'red'
    elif "blue" in wordList:
        x = 'blue'    
    elif "orange" in wordList:
        x = 'orange'    
    elif "yellow" in wordList:
        x = 'yellow'    
    elif "black" in wordList:
        x = 'black'    
    elif "violet" in wordList:
        x = 'violet'        
    else:
        x = 'black'
    color_shape.star("black",x,20*int22)
    
elif 'design' in wordList:
    if "red" in wordList:
        x = 'red'
    elif "blue" in wordList:
        x = 'blue'    
    elif "orange" in wordList:
        x = 'orange'    
    elif "yellow" in wordList:
        x = 'yellow'    
    elif "black" in wordList:
        x = 'black'    
    elif "violet" in wordList:
        x = 'violet'        
    else:
        x = 'black'
        
    color_shape.design(x)
    
else:
    print("INVALID")
        

        
        
        
        



