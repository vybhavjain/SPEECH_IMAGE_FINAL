import turtle

# color : outline color
# color1 : filler

def circle(radius,color,color1):
    turtle.color(color,color1)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
def square1(length,color,color1):
    turtle.color(color,color1)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()
        
def rectangle1(dim1,dim2,color,color1):
    turtle.color(color,color1)
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(dim1)
        turtle.left(90)
        turtle.forward(dim2)
        turtle.left(90)
    turtle.end_fill()
    
def star(color,color1,radius):
    turtle.color(color,color1)
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    
    
def design(x):   
    turtle.color(x)
    for i in range(50):
        turtle.forward(100)
        turtle.left(123)
   
def polygon(n,length,color,color1):
    turtle.color(color,color1)
    turtle.begin_fill()
    edges = n
    length1 = length
    angle = 360.0 / edges
    for i in range(n):
        turtle.forward(length1)
        turtle.right(angle)
    turtle.end_fill()
    turtle.done()
    
#circle(20,'brown','dark sea green')
#turtle.done()
#print('finished')

'''
Acceptable color list: 
['alice blue', 'antique white', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanched almond', 'blue',
 'blue violet', 'brown', 'burly wood', 'cadet blue', 'chartreuse', 'chocolate', 'coral', 'cornflower blue', 'cornsilk',
 'crimson', 'cyan', 'dark blue', 'dark cyan', 'dark golden rod', 'dark gray', 'dark grey', 'dark green', 'dark khaki', 
 'dark magenta', 'dark olive green', 'dark orange', 'dark orchid', 'dark red', 'dark salmon', 'dark sea green', 'dark slate blue',
 'dark slate gray', 'dark slate grey', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dim grey',
 'dodger blue', 'fire brick', 'floral white', 'forest green', 'fuchsia', 'gainsboro', 'ghost white', 'gold', 'golden rod', 
 'gray', 'grey', 'green', 'green yellow', 'honey dew', 'hot pink', 'indian red', 'indigo', 'ivory', 'khaki', 'lavender',
 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light golden rod yellow',
 'light gray', 'light grey', 'light green', 'light pink', 'light salmon', 'light sea green', 'light sky blue',
 'light slate gray', 'light slate grey', 'light steel blue', 'light yellow', 'lime', 'lime green', 'linen', 
 'magenta', 'maroon', 'medium aqua marine', 'medium blue', 'medium orchid', 'medium purple', 'medium sea green',
 'medium slate blue', 'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 
 'misty rose', 'moccasin', 'navajo white', 'navy', 'old lace', 'olive', 'olive drab', 'orange', 'orange red', 'orchid',
 'pale golden rod', 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'peru', 'pink', 'plum', 
 'powder blue', 'purple', 'rebecca purple', 'red', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'sandy brown',
 'sea green', 'sea shell', 'sienna', 'silver', 'sky blue', 'slate blue', 'slate gray', 'slate grey', 'snow', 'spring green',
 'steel blue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'white smoke', 'yellow', 'yellow green']
'''