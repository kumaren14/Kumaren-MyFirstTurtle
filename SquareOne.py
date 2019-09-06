import turtle

turtle.speed(100)
turtle.color("red")

def square(turtle, sidelength):
    for i in range(4):
        turtle.right(90)
        turtle.forward(sidelength)

for i in range(60):
    square(turtle,75)
    turtle.right(5)

turtle.exitonclick()