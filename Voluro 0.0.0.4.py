import time as ti

print("Welcome to Voluro.py no-gui 0.0.0.4.0")
loaded = False
print("loading")
while loaded != True:
    pcname = "Voluro"


    def reset():
        print("setting up basevars...")
        global pcname, help
        help = '''
        help: Display all the commands and meanings
        basevar: Sets one of the basevar to a new value. Can use --pcname to rename your pc
        reset: Resets the system to it's defaults. All customizations will be lost
        exit: Closes Voluro
        launch: Launches a program. Use '--' and the program name
        listapps: Lists all your apps
        '''
        pcname = "Voluro"
        global pos
        global running
        print("setting up apps...")
        global apps
        global running
        apps = ['clock']

        def clock():
            print("The time is:")
            print(ti.asctime(ti.localtime()))

        def runpcname():
            global pcname
            running =True
            while running:
                print("enter your new pc name")
                inpt = input("@" + pcname + ":" + 'pcname' +':')
                if len(inpt.split()) == 1:
                    pcname = inpt.split()[0]
                    running = False
                else:
                    print("error code 2 - invalid input")
                running = False

        global runapp

        def runapp(id):
            running = True
            if id == 0:
                clock()
            running = False
        # here go the rest of the configs


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
    elif inptlen >= 3:
        if (inpt.split())[1] == '--pcname':
            try:
                runpcname()
            except:
                print("To change your pc's name, you have to specify another name.")
    elif inptlen == 2:
        if (inpt.split())[0] == 'launch':
            j = 0
            for i in apps:
                if (inpt.split())[1] == "--" + apps[j]:
                    runapp(j)
                j = j + 1
    elif inpt == 'listapps':
        print(apps)
    else:
        print("error code 1 - unknown command - invalid syntax")
