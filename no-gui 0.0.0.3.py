import time as ti
import turtle as t

#print("Welcome to Voluro.py no-gui 0.0.0.2")
t.speed(0)
text = ""
t.hideturtle()
style = ("Segoe UI Light", 11)
list = ["W", "e", "l", "c", "o", "m", "e", " ", "t", "o", " ", "V",
        "o", "l", "u", "r", "o", " ", "0", ".", "0", ".", "0", ".", "2"]
t.pu()
t.setpos(-100, 300)
for i in range(len(list)):
    text = text + list[i]
    t.write(text, font=style)
    ti.sleep(0.05)
#loader
loaded = False
t.pu()
t.setpos(-15, 0)
t.write("loading", font=style)
while loaded != True:
    pcname = "Voluro"
    loaded = True
#main
t.clear()
if t.textinput("cmd", "Enter a command") == "help": # help
    print("help")
t.exitonclick()
