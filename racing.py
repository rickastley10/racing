import turtle as t
import random
t.tracer(0, 0)
t.delay(0)
t.penup()
carx, cary = 0, -100
obstx, obsty = 0, 300
lane = 1
score = 0
speed = 20
laney = 400
t.setup(400, 600)
t.title("racing")

t.hideturtle()
t.pencolor("red")
t.fillcolor("red")
t.bgcolor("black")
def car():
    t.goto(carx, cary)
    t.pencolor("red")
    t.fillcolor("red")
    t.pendown()
    t.begin_fill()
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.end_fill()
    t.penup()

def obstacle():
    t.goto(obstx, obsty)
    t.pencolor("blue")
    t.fillcolor("blue")
    t.pendown()
    t.begin_fill()
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.end_fill()
    t.penup()

def movobst():
    global obstx, obsty, lane, score
    obsty -= speed
    global lane
    if obsty < -300:
        obsty = 300
        lane = random.randint(1, 3)
        score += 1
        if lane == 1:
            obstx = -100
        elif lane == 2:
            obstx = 0
        elif lane == 3:
            obstx = 100
    if cary < obsty < cary + 60 and carx == obstx:
        score = 0
        obsty = 300
        obstx = 0

def lanes():
    global laney
    t.fillcolor("red")
    t.goto(50, laney)
    t.right(90)
    for _ in range(60):
        t.pencolor("white")
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(5)
    t.goto(-50, laney)
    for _ in range(60):
        t.pencolor("white")
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(5)
    t.left(90)
    laney += 10
    if laney >= 400:
        laney = 300
def right():
    global carx
    if carx < 100:
        carx += 100

def left():
    global carx
    if carx > -100:
        carx -= 100

def click(x, y):
    if 0 < x:
        right()
    elif x < 0:
        left()
def scoreboard():
    t.fillcolor("red")
    t.goto(0, 0)
    t.pencolor("red")
    t.write(f"{score}", font=("Arial", 16, "normal"))


t.onscreenclick(click)
t.onkey(left, "Left")
t.onkey(right, "Right")
t.onkey(left, "a")
t.onkey(right, "d")
t.listen()
def mainloop():
    t.pencolor("red")
    t.clear()
    t.update()
    car()
    obstacle()
    movobst()
    scoreboard()
    lanes()
    t.ontimer(mainloop, 30)

mainloop()
t.mainloop()
