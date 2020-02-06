#my_flower.py (finsished) 
#Last edited: 12/30/2019
#Draw a petal and so going on a flower
#by: Tran Dat Tin

import math
import turtle

def draw_arc(t,radius,angle):
    '''
    Set out and draw the arc  
    t: turtle
    angle: the size of the petal (units degree)
    radius: the length of the petal    '''
    #set out the arc of the petal   
    arc_length = 2*math.pi*radius*abs(angle)/360 
    #divise arc to many parts to make the turtle faster
    n = int(arc_length/4)+1
    #set step of small length equal to arc_length for n time
    step_length= arc_length/n
    #set step of small angle depend on the arc's angle of petal    
    step_angle = float(angle)/n
    #start draw
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def draw_a_petal(t,angle,radius):
    '''
    Draw a petal by draw arc for two times
    t: turtle
    angle: the size of the petal (units degree)
    radius: the length of the petal    '''
    for i in range(2):
        draw_arc(t,radius,angle)
        #Move the turtle depends on the size of petal (big angle => big petal)
        t.lt(180-angle)

def draw_a_flower(t,angle,n_petal,radius):
    '''
    Draw a full flower by draw petal n time
    angle: the size of flower (units degree)
    radius: the length of the petal    '''
    for i in range(n_petal):
        draw_a_petal(t,angle,radius)
        #Make sure all the petals display evenly
        t.lt(360/n_petal)

def draw_flowers(t,angle,n_petal,radius):
    ''' Draw a flower and move for the next flower
    '''
    draw_a_flower(t,angle,n_petal,radius)
    t.pu()
    t.fd(radius*2 + 10)
    t.pd()

bob = turtle.Turtle()

size = 70
draw_flowers(bob,100,10,size)

bob.hideturtle()
turtle.mainloop()


