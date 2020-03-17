import turtle #import modules

ob = turtle.Turtle() #creat the object with the turtle function
ob.speed(0) #object's speed how faster the shape will complate 

cl = ["red","green","blue"] #colours of the shape, 0, 1, 2

def drawArt(d,angle,x,y): #creat a def function and add the distance with the angle and  we called them paraqmeters 
  c = 0 #varible
  ob.up() #move the object up 
  ob.goto(x,y)
  ob.down() #move the object down
  for i in range(1,400): #forloop, declare a varible called i, changed from 1 to 400 
    ob.pencolor(cl[c]) #pen colour 
    ob.forward(d) #the direction of the object
    ob.left(angle) # the direction of the  object 
    d = d - 1 #d: distance 
    c = c + 1 #c: to keep the colours changing 
    if(c>2): #if statment 
      c = 0 #c start again with the color red 

drawArt(150,98,0,0) #run the function 