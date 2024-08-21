from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
h = 0.1

for i in range(180):
    c = cs.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.004
    fd(100)
    rt(30)
    fd(20)
    rt(30)
    fd(50)
    rt(30)
    goto(0,0)
    rt(2)
done()
