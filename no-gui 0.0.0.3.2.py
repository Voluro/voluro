import time as ti
print("Welcome to Voluro.py no-gui 0.0.0.3.2")
loaded = False
print("loading")
while loaded != True:
    pcname = "Voluro"
    loaded = True
print("done")
print("type help for help")
while True:
    inpt = input("@" + pcname + ":")
    inptlen = len(split(inpt))
    if inpt == 'help':
        print("current commands: \nhelp: display all the commands and meanings\nbasevar: sets one of the basevars to a new value. Can use --pcname to change the pcname.")
    if inptln =< 3:
        if (split(inpt))[0] == 'basevar':
            if (split(inpt))[1] == '--pcname':
                pcname = (split(inpt))[2]
