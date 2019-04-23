 #Turtle Graphics Game
import turtle
import math
import random

#Set up screen
wn = turtle.Screen()
wn.bgcolor("#dddd99")

#Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()    

#Create player turtle
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)

#Create goal
goal = turtle.Turtle()
goal.color("blue")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-100, -100)

#Set speed variable
speed = 3

#Define functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def isCollision(t1, t2):
     d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
     if d < 20:
         return True
     else:
         return False
        
    
#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")

while True:
    player.forward(speed)

    #Boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(100)

    #Boundary Checking
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(100)

    #Collision checking
    if isCollision(player, goal):
        goal.set.position(random.randint(-300, 300), random.randint(-300, 300))

