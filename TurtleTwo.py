import turtle
import time

turtle.shape("turtle")

turtle.speed(7)

turtle.pensize(5)
turtle.color("saddlebrown")
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(45)
turtle.begin_fill()
turtle.color("firebrick")
turtle.forward(90)
turtle.right(90)
turtle.forward(90)
turtle.right(45)
turtle.end_fill()
turtle.color("saddlebrown")
turtle.forward(100)
turtle.right(90)
turtle.forward(27)
turtle.forward(35)
turtle.right(90)
turtle.color("peru")
turtle.forward(65)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(65)
turtle.color("saddlebrown")
turtle.left(90)
turtle.forward(65)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(27)
turtle.backward(27)
turtle.left(120)
turtle.color("brown")
turtle.begin_fill()
turtle.forward(73)
turtle.right(165)
turtle.forward(90)
turtle.right(135)
turtle.forward(27)
turtle.end_fill()

turtle.penup()
turtle.color("black")

turtle.forward(250)
turtle.write("Hello World!")
turtle.left(90)
turtle.forward(25)
turtle.write("Kumaren Anand")
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.right(180)
time.sleep(1)
turtle.color("turquoise")
turtle.speed(5)
turtle.right(360)
turtle.color("black")




turtle.exitonclick()