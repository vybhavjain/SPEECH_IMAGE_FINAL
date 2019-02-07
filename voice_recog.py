import turtle
import speech_recognition as sr
import re
from flowchart_addsubmuldiv import flowchart
#import comparator
import color_shape

import urllib.request
from bs4 import BeautifulSoup


def getColors():
    html = urllib.request.urlopen('http://www.w3schools.com/colors/colors_names.asp').read()
    soup = BeautifulSoup(html, 'html.parser')
    children = [item.findChildren() for item in soup.find_all('tr')]
    colors = [''.join( ' '+x if 'A' <= x <= 'Z' else x for x in item[0].text.replace(u'\xa0', '')).strip().lower() for item in children]
    return colors[1:]


def findmatches(pattern, phrase):

    for p in patterns:
        match= re.findall(p, phrase)
        return match
  
list1 = getColors()  # List of all possible colors
list2 = []


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

for i in wordList:
    if i in list1:
        list2.append(i)

if 'circle' in wordList:
    color_shape.circle(20*int22,list2[0],list2[1])
    
elif 'square' in wordList:
    color_shape.square1(20*int22,list2[0],list2[1])
    
elif 'rectangle' in wordList:
    color_shape.rectangle1(20*int22,(20*int22)/2,list2[0],list2[1])
    
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
    color_shape.star(list2[0],list2[1],20*int22)
    
elif 'design' in wordList:
    color_shape.design(list2[0])
    
else:
    print("INVALID")
   
turtle.hideturtle()
turtle.done()
     

        
        
        
        



