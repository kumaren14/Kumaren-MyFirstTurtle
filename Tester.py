import turtle

turtle.penup()
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



turtle.exitonclick()