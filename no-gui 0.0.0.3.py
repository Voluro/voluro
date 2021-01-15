import time as ti
print("Welcome to Voluro.py no-gui 0.0.0.2")
loaded = False
print("loading")
while loaded != True:
    pcname = "Voluro"
    loaded = True
print("done")
print("type help for help")
while True:
    inpt = input("@" + pcname + ":")
    if inpt == 'help':
        print("current commands: \nhelp: display all the commands and meanings")
