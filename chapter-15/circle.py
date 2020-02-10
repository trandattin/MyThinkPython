'''
Exercise 15.1. Write a definition for a class named Circle with attributes center and radius ,
where center is a Point object and radius is a number.

Instantiate a Circle object that represents a circle with its center at ( 150, 100 ) and radius 75.
Write a function named point_in_circle that takes a Circle and a Point and returns True if the
Point lies in or on the boundary of the circle.

Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if
the Rectangle lies entirely in or on the boundary of the circle.

Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns

True if any of the corners of the Rectangle fall inside the circle. Or as a more challenging version,
return True if any part of the Rectangle falls inside the circle.
'''

import math
import copy 

class Point:
    '''Represents a point in 2-D space.'''
    

def print_point(p):
    '''Print a Point object in human-readable format.'''
    return ('(%g, %g)' % (p.x, p.y))


class Circle:
    '''Represents a circle.

    Attributes: center, radius
    '''

class Rectangle:
    '''Represents a rectangle.

    attributes: width, height, corner
    '''

def distance_between_points(p1,p2):
    '''Computes distance between two points

    p1, p2: Point object
    '''
    dx = p1.x - p2.x
    dy = p1.y -p2.y
    return math.sqrt(dx**2 + dy**2)


def point_in_circle(point,circle):
    ''' Checks whether a point lies inside a circle (or on the boundary)

    point: Point object
    circle: Circle object
    '''
    d = distance_between_points(point, circle.center)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    '''Checks whether the corners of a rect fall in/on a circle
    
    rect: Retangle object
    circle: Circle object
    '''

    p = copy.copy(rect.corner)

    if not point_in_circle(p, circle):
       return False
    
    p.x += rect.width
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    if not point_in_circle(p, circle):
        return False
    
    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False
    
    return True
    

def rect_in_circle_overlap(rect, circle):
    ''' Checks whether any corners of a rect fall in/on a circle/

    rect: Rectangle object
    circle: Circle object
    '''
    p = copy.copy(rect.corner)

    if point_in_circle(p, circle):
        return True
    
    p.x += rect.width
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    if point_in_circle(p, circle):
        return True
    
    return False

    
def main():
    circle = Circle()
    circle.center = Point()
    circle.center.x = 5
    circle.center.y = 6
    circle.radius = 70

    p = Point()
    p.x = 9
    p.y = 10

    rect = Rectangle()
    rect.height = 10
    rect.width = 50
    rect.corner = Point()
    rect.corner.x = 0
    rect.corner.y = 0

    print(rect_in_circle_overlap(rect, circle))

if __name__ == "__main__":
    main()