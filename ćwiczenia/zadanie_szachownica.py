import turtle

"""setheading

0 - east

90 - north

120 - west

270 - south
"""

turtle.speed(0)

def move_up(steps = 60):



turtle.setheading(90)
turtle. forward(60)

turtle.setheading(0)
turtle. forward(60)

turtle.setheading(270)
turtle. forward(60)

turtle.setheading(180)
turtle. forward(60)

for i in range(20):
    turtle.setheading(90)
    turtle.forward(60)
    turtle.setheading(0)
    turtle.forward(1)
    turtle.setheading(270)
    turtle.forward(60)
    turtle.setheading(1)




turtle.done()