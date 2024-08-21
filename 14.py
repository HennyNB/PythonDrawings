from turtle import *
import colorsys as cs
bgcolor('black')
tracer(2)
pensize(2)
h = 0

for i in range(500):
    c = cs.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.008
    right(90)
    forward(i)
    circle(1 * 2, - 10)
    left(120)
    up()
    forward(i)
    down()
    circle(i * 2, - 90)
done()
