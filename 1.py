import turtle as t
import colorsys as cs
t.bgcolor('black')
color = ['steelblue','coral','magenta','palegreen']
for i in range(200):
    t.pencolor(color[i%4])
    t.rt(i)
    t.circle(120,i)
    t.fd(i)
    t.rt(90)
t.done()
