from turtle import *
import colorsys as cs

bgcolor('black')
tracer(10)
pensize(4)
h = 0

for i in range(200):
    c = cs.hsv_to_rgb(h, 1, 1)
    h += 0.01  
    fillcolor(c)
    pencolor('black')

    begin_fill()

    fd(i)
    rt(67)
    fd(i)
    circle(i, 30)
    fd(i)
    lt(190)

    end_fill()

done()