import time as ti
import keyboard
print("Welcome to Voluro.py no-gui 0.0.0.4.0")
loaded = False
print("loading")
while loaded != True:
    def reset():
        global pcname
        global help
        help = '''
        help: Display all the commands and meanings
        basevar: Sets one of the basevar to a new value. Can use --pcname to rename your pc
        reset: Resets the system to it's defaults. All customizations will be lost
        exit: Closes Voluro
        launch: Launches a program. Use '--' and the program name
        listapps: Lists all your apps
        '''
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
        print(help)
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
    elif inptlen <= 3:
        if (inpt.split())[0] == 'basevar':
            if (inpt.split())[1] == '--pcname':
                pcname = (inpt.split())[2]
                #try:
                #    pcname = (inpt.split())[2]
                #except:
                #    print("To change your pc's name, you have to specify another name.")
                #    print("Do you need further help with this command?(y/n)")
                #    temp = input()
                #    if temp == "y":
                #        print("This command is used like this: basevar --pcname putyournamehere(no spaces are allowed)")
    else:
        print("Command execution failed. Type help to see all commands.")