import math
import copy
class Point:
    '''Represents a point in 2-D space.'''

def print_point(p):
    print ('(%g, %g)' % (p.x, p.y))

def distance_between_points(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx**2 + dy**2)

class Rectangle():
    '''represent a rectangle.
       attributes: width, height, coner.
    '''
def find_center(box):
    p = Point()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y + box.height/2.0
    return p 

def grow_rectangle(rect,dwidth,dheight):
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect,dx,dy):
    rect.corner.x += dx
    rect.corner.y += dy 

def move_rectangle_copy(rect,dx,dy):
    new = copy.deepcopy(rect)
    move_rectangle(new,dx,dy)
    return new
    

blank = Point()
blank.x = 3.0
blank.y = 4.0

grosse = Point()
grosse.x = 3.0
grosse.y = 5.0

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

grow_rectangle(box,50,100)

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

grow_rectangle(box,50,100)
move_rectangle(box,3,4)

new_box = move_rectangle_copy(box,3,5)

print(new_box.corner.x)
print(new_box.corner.y)

