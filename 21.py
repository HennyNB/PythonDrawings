from turtle import *
import colorsys
tracer(2)
bgcolor('black')
pensize(2)
h = 0.3

for i in range(500):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.005
    rt(20)
    for j in range(5):
        fd(i)
        rt(100)
        rt(50)
        rt(118)
done()
