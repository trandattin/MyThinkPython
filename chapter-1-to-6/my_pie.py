#my_pie.py (finished)
#Last edited: 12/30/2019
#Go draw a pie from n triangles 
#A pie have the polygon shape
#by: tran_dat_tin

import turtle
import math

def draw_isosceles(t,radius,exterior_angle):
    '''Draw an isosceles triangle
       t : turtle
       angle: exterior angle of a polygon
    '''
    # Tính một nửa cạnh ngoài đa giac (sin đi học)
    a_half_chord = radius * math.sin((exterior_angle/2) * math.pi / 180)
    # Hạ một nửa góc để bắt đầu vẽ
    t.lt(exterior_angle/2)
    # Vẽ cạnh đều của tam giác bằng = radius
    t.fd(radius)
    # Nghiêng góc
    t.lt(90+(exterior_angle/2))  
    # Vẽ cạnh ngoài của đa giác (a chord)
    t.fd(a_half_chord*2)  
    # Nghiêng góc 
    t.lt(90+(exterior_angle/2)) 
    # Vẽ cạnh đều thứ 2 của tam giác bằng = radius
    t.fd(radius)
    # Quay con rùa bằng 180 độ rồi bù trừ cho dòng code 25
    t.lt(180-(exterior_angle/2))

def polypie(t,n_slide,radius):
    '''Draws a pie divided into radial segments
    '''
    exterior_angle = 360/n_slide
    for i in range(n_slide):
        draw_isosceles(t,radius,exterior_angle)

def draw_pie(t,n_slide,radius):
    """Draws a pie, then moves into position to the right.
    t: Turtle
    n_slide: number of segments
    radius: length of the radial spokes
    """
    polypie(t,n_slide,radius)
    t.pu()
    t.fd(radius*2+10)
    t.pd()

bob = turtle.Turtle()

# draw polypies with various number of sides
size = 40
draw_pie(bob,5,size)
draw_pie(bob,6,size)
draw_pie(bob,8,size)

bob.hideturtle()
turtle.mainloop()