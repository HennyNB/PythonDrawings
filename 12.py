from turtle import *
import colorsys
bgcolor('black')
tracer(20)
pensize(5)

h = 0

for i in range(400):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    goto(0,0)
    color(c)
    circle(10)
    forward(400 - i)
    lt(20)
    circle(10)
    rt(10)
done()
