import turtle

turtle.color("green")

turtle.penup()
turtle.goto(-300, -200)
turtle.pendown()

turtle.speed(100)

size = 0

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

for i in range(80):
    star(turtle, 50)
    turtle.right(5)
    size += 2

turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()

turtle.color("purple")

size = 0

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

for i in range(80):
    star(turtle, 50)
    turtle.right(5)
    size += 2

turtle.penup()
turtle.goto(200, 100)
turtle.pendown()

turtle.color("orange")

size = 0

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

for i in range(80):
    star(turtle, 50)
    turtle.right(5)
    size += 2


turtle.exitonclick()