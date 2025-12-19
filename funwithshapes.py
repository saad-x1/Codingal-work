import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.speed(3)

def draw_polygon(sides, length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()

t.penup()
t.goto(-200, 0)
t.pendown()
draw_polygon(3, 100, "red")

t.penup()
t.goto(0, 0)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

t.penup()
t.goto(200, 0)
t.pendown()
draw_polygon(6, 80, "yellow")

turtle.done()
