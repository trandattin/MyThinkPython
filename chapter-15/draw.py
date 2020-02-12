'''Exercise 15.2. Write a function called draw_rect that takes a Turtle object and a Rectangle and
uses the Turtle to draw the Rectangle. See Chapter 4 for examples using Turtle objects.
Write a function called draw_circle that takes a Turtle and a Circle and draws the Circle.
Solution: http: // thinkpython2. com/ code/ draw. py .
'''

import turtle

import polygon

from circle import Circle, Point, Rectangle

def draw_rect(t, rect):
    ''' Move the turtle in (x,y) and draw a rect.
    t : turtle
    rect: Rectangle object
    '''
    t.pu()
    t.goto(rect.corner.x,rect.corner.y)
    t.setheading(0)
    t.pd()

    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)

def draw_circle(t, circle):
    '''Move the turtle in (x,y) and draw a circle
    t: turtle
    circle: Circle object
    '''
    t.pu()
    t.goto(circle.corner.x, circle.corner.y)
    t.fd(circle.radius)
    t.lt(90)
    t.pd()
    polygon.circle(t, circle.radius)

if __name__ == "__main__":
    t = turtle.Turtle()

    #draw the axe:
    length = 400
    t.fd(length)
    t.bk(length)
    t.lt(90)
    t.fd(length)

    #draw rectangle
    rect = Rectangle()
    rect.width = 100
    rect.height = 200
    rect.corner = Point()
    rect.corner.x = 30.0
    rect.corner.y = 100.0

    #draw circle
    circle = Circle()
    circle.radius = 200
    circle.corner = Point()
    circle.corner.x = 0.0
    circle.corner.y = 0.0
    #draw_rect(t, rect)
    draw_circle(t, circle)