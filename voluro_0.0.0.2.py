import turtle as t
import time as ti
import random as r

def sayfact(x, y, color):
    prex = t.xcor()
    prey = t.ycor()
    style = ("Segoe UI Light", 11, 'italic')
    t.pu()
    t.setpos(x, y)
    t.color(color)
    t.pd
    facts = ["The loading icon was created by accident!", "This version is still indev!", "If you are viewing this you are the one of the two people that created this!"]
    t.write(facts[r.randrange(len(facts))-1], font=style)
    t.pu
    t.setpos(prex, prey)

t.speed(0)
text = ""
t.hideturtle()
style = ("Segoe UI Light", 11)
list = ["W", "e", "l", "c", "o", "m", "e", " ", "t", "o", " ", "V",
        "o", "l", "u", "r", "o", " ", "0", ".", "0", ".", "0", ".", "2"]
t.pu()
t.setpos(-100, 75)
for i in range(len(list)):
    text = text + list[i]
    t.write(text, font=style)
    ti.sleep(0.05)
t.pu()
t.setpos(-15, -125)
t.write("loading...", font=style)
t.pu()
t.setpos(0, -20)
t.pd()
sayfact(-75, -160, "#000000")
while True:
    t.color('blue')
    for i in range(23):
        t.forward(8)
        t.right(15)
    t.color('white')
    for i in range(23):
        t.forward(8)
        t.right(15)
    t.pu()
    t.setpos(-15, -125)
    t.color('#000000')
    t.write("loading...", font=style)
    t.pu()
    t.setpos(0, -20)
    t.pd()
