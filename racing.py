import turtle as t
t.setup(300, 500)
carx = -100
line = 1
t.penup()
obst1x = -100
obststart= 200
obsty = obststart
t.hideturtle()
t.tracer(0, 0)
import random
cary = -100
def car():
    if line == 1:
        carx= -100
    elif line ==2:
        carx=100
    t.clear()
    t.goto(carx, cary)
    t.pendown()
    t.setheading(90)
    t.begin_fill()
    t.forward(40)
    t.right(45)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(45)
    t.forward(40)
    t.right(90)
    t.forward(29)
    t.end_fill()
    t.penup()

    global obsty
    global mobsty
    mobsty = obsty - 20
    obsty=mobsty
    t.ontimer(obstacle() ,200)
    t.update()

def obstacle( ):
    global obsty, obst1x
    t.goto( obst1x + 40, obsty)
    t.pendown()
    t.begin_fill()
    
    for yaidaiouwhu in range(4):
        t.forward(40)
        t.right(90)
    t.end_fill()
    
    t.penup()

    if obsty == -120:
        obsty = obststart
        global randint
        randint = random.randint(1, 2)
        #print(randint)
        if randint == 1:
            obst1x = -100

        elif randint ==2:
            obst1x = 100
    
    

    if line == 1:
        current_carx = -100
    else:
        current_carx = 100
    
    if obst1x == current_carx and cary <= obsty <= cary + 40:
        quit()
            
        


def left():
    
    global line
    if line == 2:
        line = 1
        car()
    
def right():
    global line
    if line == 1:
        line = 2
        car()

def autoswitch(x, y):
    global line
    if line == 1:
        line = 2
        car()
        
    elif line == 2:
        line = 1
        car()
car()
t.onscreenclick(autoswitch)

t.onkey(left, "a")
t.onkey(right, "d")

t.listen()
while 1== 1:
    car()
t.mainloop()
