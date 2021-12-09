import turtle

s = turtle.Screen()
turt=turtle.Turtle()

#B

turt.color('green')
turt.shape('turtle')
turt.pensize(5)
turt.goto(-750,0)
turt.right(90)
turt.forward(180)
turt.left(90)
turt.forward(10)
turt.circle(45,195)
turt.penup()
turt.right(105)
turt.forward(90)
turt.pendown()
turt.right(90)
turt.circle(-45,180)
turt.penup()

turt.left(90)
turt.forward(90)
turt.left(90)
turt.forward(180)


#O

turt.pendown()
turt.circle(90,360)
turt.penup()

turt.forward(130)
turt.left(90)
turt.forward(180)


#B

turt.pendown()
turt.left(180)
turt.forward(180)
turt.left(90)
turt.forward(10)
turt.circle(45,195)
turt.penup()
turt.right(105)
turt.forward(90)
turt.pendown()
turt.right(90)
turt.circle(-45,180)
turt.penup()

turt.left(90)
turt.forward(90)
turt.left(90)
turt.forward(130)

#E

turt.pendown()
turt.left(90)
turt.forward(180)
turt.right(90)
turt.forward(45)
turt.backward(45)
turt.right(90)
turt.forward(90)
turt.left(90)
turt.forward(45)
turt.backward(45)
turt.right(90)
turt.forward(90)
turt.left(90)
turt.forward(45)
turt.backward(45)
turt.penup()

turt.forward(90)
turt.left(90)

#H

turt.pendown()
turt.forward(180)
turt.backward(90)
turt.right(90)
turt.forward(50)
turt.left(90)
turt.forward(90)
turt.backward(180)
turt.penup()

turt.right(90)
turt.forward(50)
turt.left(90)
turt.forward(180)

#U

turt.pendown()
turt.backward(150)
turt.circle(-30,-180)
turt.left(180)
turt.forward(150)
turt.penup()

turt.backward(180)
turt.right(90)
turt.forward(45)

#D

turt.pendown()
turt.left(90)
turt.forward(180)
turt.right(90)
turt.circle(-90,180)

s.exitonclick()