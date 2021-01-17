import webbrowser
import savedsettings
print("Welcome to Voluro.py no-gui 0.0.1.0")
loaded = False
print("loading")
while loaded != True:
    def reset():
        print("setting up basevars...")
        global pcname1, help
        help = '''
        help: Display all the commands and meanings.
        basevar: Sets one of the basevars to a new value. Can use --pcname to rename your pc.
        reset: Resets the system to it's defaults. All customizations will be lost.
        exit: Closes Voluro.
        launch: Launches a program.
        listapps: Lists all your apps.
        adap: adds the specified app.
        inap: opens the page for installing apps (Requires internet connection).
        '''

        global pos
        global running
        print("setting up apps...")
        global apps
        global running
        apps = []
        # here go the rest of the configs
        print('loading previous settings')
        pcname1 = str(savedsettings.load("pcname"))
    reset()
    loaded = True

print("done")
print("type help for help")
while True:
    inpt = input("@" + pcname1 + ":")
    inptlen = len(inpt.split())
    if inpt == 'help':
        print(help)
    elif inpt == 'reset':
        print("Are you sure?(y/n)")
        temp = input()
        if temp == 'y':
            reset()
            savedsettings.save('pcname', 'Voluro')
        else:
            pass
    elif inpt == 'exit':
        exit()
    elif inptlen == 2:
        if (inpt.split())[1] == '--pcname':
            pcname.pcname()
    elif inptlen == 2:
        if (inpt.split())[0] == 'launch':
            try:
                exec(inpt.split()[1] + "." + inpt.split()[1] + "()")
            except:
                print("error code 3 - invalid app")
        elif (inpt.split())[0] == 'adap':
            try:
                exec('import' + " " + inpt.split()[1])
                print('app ' + inpt.split()[1] + ' added')
                apps.append(inpt.split()[1])
            except:
                print("error code 3 - invalid app")
    elif inpt == 'inap':
        try:
            webbrowser.open('voluro.github.io')
            print('app ' + inpt.split()[1] + ' added')
        except:
            print("error code 4 - error in getting app")
    elif inpt == 'listapps':
        for b in apps:
            print(b)
    else:
        print("error code 1 - unknown command - invalid syntax")

