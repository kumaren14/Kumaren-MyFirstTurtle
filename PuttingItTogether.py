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
turtle.goto(200, 100)
turtle.pendown()

turtle.speed(100)
turtle.color("red")

def square(turtle, sidelength):
    for i in range(4):
        turtle.right(90)
        turtle.forward(sidelength)

for i in range(72):
    square(turtle,75)
    turtle.right(5)

turtle.penup()
turtle.goto(-300, 250)
turtle.color("firebrick")
turtle.pendown()

turtle.speed(7)
turtle.pensize(5)

turtle.left(40)

turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)


turtle.penup()
turtle.goto(0, 0)
turtle.right(90)

turtle.goto(200, -250)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

turtle.penup()
turtle.color("black")
turtle.goto(175, -175)
turtle.pendown()

turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(225, -175)
turtle.pendown()

turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-50, 0)
turtle.write("A collection of shapes")
turtle.goto(-100, -20)
turtle.write("An art gallery by Kumaren Anand")





turtle.exitonclick()