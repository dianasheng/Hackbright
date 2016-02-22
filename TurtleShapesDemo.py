import turtle

#demo of turtle graphics

window = turtle.Screen()
window.bgcolor("red")

def draw_square(new_turtle):
    for x in range(0,4):
        new_turtle.right(90)
        new_turtle.forward(100)

#create an instance of Turtle
fred = turtle.Turtle()
#set values on attributes in the Turtle module
fred.shape("turtle")
fred.color("green")
fred.setx(-100)

#create an instance of Turtle
toto = turtle.Turtle()
toto.shape("turtle")
toto.color("blue")
toto.setx(100)

#draw offset squares in a loop
for x in range(0,36):
    draw_square(fred)
    fred.right(10)

#draw offset circles in a loop
for x in range (0, 18):
    toto.circle(50)
    toto.right(20)

window.exitonclick()
