import time as ti
import keyboard
print("Welcome to Voluro.py no-gui 0.0.0.4.0")
loaded = False
print("loading")
while loaded != True:
    def reset():
        global pcname
        pcname = "Voluro"
        #here go the rest of the configs
    reset()
    loaded = True
print("done")
print("type help for help")
while True:
    inpt = input("@" + pcname + ":")
    inptlen = len(inpt.split())
    if inpt == 'help':
        print("help: Display all the commands and meanings\nbasevar: Sets one of the basevar to a new value. Can use --pcname to rename your pc\nreset: Resets the system to it's defaults. All customizations will be lost\nexit: Closes Voluro\nlaunch: Launches a program. Use '--' and the program name\nlistapps: Lists all your apps")
    elif inpt == 'reset':
        print("Are you sure?(y/n)")
        temp = input()
        if temp == 'y':
            reset()
        else:
            pass
    elif inpt == 'exit':
        exit()
    elif inptlen <= 3:
        if (inpt.split())[0] == 'launch':
            if (inpt.split())[1] == "--clock":
                print("Clock. Press 's' to stop.")
                while True:
                    print(ti.asctime(ti.localtime()), end="\r", flush=True)
                    if keyboard.is_pressed('s'):
                        break
                print()
        elif (inpt.split())[1] == '--pcname':
            try:
                pcname = (inpt.split())[2]
            except:
                print("To change your pc's name, you have to specify another name.")
                print("Do you need further help with this command?(y/n)")
                temp = input()
                if temp == "y":
                    print("This command is used like this: basevar --pcname putyournamehere(no spaces are allowed)")
    elif inpt == 'listapps':
        print("clock")
    else:
        print("error code 1 - unknown command - invalid syntax")
