import turtle

from circle import Point, Rectangle, Circle

import polygon

def draw_rect(t, rect):
    '''Draws  rectangle.

    t: turtle
    rect: Rectangle'''
    "python.pythonPath": "python3"
    
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0)
    t.pd()  

    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)


if __name__ == "__main__":
    bob = turtle.Turtle()

    length = 400
    bob.fd(length)
    bob.bk(length)
    bob.lt(90)
    bob.fd(length)
    bob.bk(length)

    #draw a rectangle
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    draw_rect(bob, box)

    turtle.mainloop()