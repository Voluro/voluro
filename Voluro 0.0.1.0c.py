import webbrowser
try:
    import savedsettings
except:
    print("you do not have the mandatory application for Voluro to run. Would you like to install it? (y/n)")
    temp = input()
    if temp == "y":
        file = open("savedsettings.py", "w")
        file.write('''
def load(name):
    file = open(f'{name}.sdss', 'r')
    file = file.read()
    return file


def save(name, val):
    file = open(f'{name}.sdss', 'w')
    file.write(val)


def append(name, val):
    file = open(f'{name}.sdss', 'a')
    file.write(val)
''')
        exit("relaunch Voluro for the specified changes to take place")
print("Welcome to Voluro.py no-gui 0.0.1.0b")
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
        -r: Launches a program.
        listapps: Lists all your apps.
        adap: adds the specified app.
        inap: opens the page for installing apps (Requires internet connection).
        exec: executes code directly.
        '''

        global pos
        global running
        print("setting up apps...")
        global apps
        global running
        global allapps
        try:
            apps = savedsettings.load('apps')
        except:
            savedsettings.save('apps', '')
            apps = savedsettings.load('apps')
        allapps = apps.split(", ")
        # here go the rest of the configs
        print('loading previous settings')
        try:
            pcname1 = str(savedsettings.load("pcname"))
        except:
            savedsettings.save("pcname", "Voluro")
            pcname1 = str(savedsettings.load("pcname"))
        exec(f'import {apps}')

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
            import pcname

            pcname.pcname()
        elif (inpt.split())[0] == '-r':
            try:
                exec(inpt.split()[1] + "." + inpt.split()[1] + "()")
            except:
                try:
                    exec('import' + " " + inpt.split()[1])
                    exec(inpt.split()[1] + "." + inpt.split()[1] + "()")
                except:
                    print("error code 3 - invalid app")
        elif (inpt.split())[0] == 'adap':
            try:
                exec('import' + " " + inpt.split()[1])
                print('app ' + inpt.split()[1] + ' added')
                savedsettings.append('apps', ', ' + inpt.split()[1])
                apps = savedsettings.load('apps')
                try:
                    allapps = apps.split(", ")
                except:
                    pass
            except:
                print("error code 3 - invalid app")
        else:
            print('error code 1 - unknown command - invalid syntax')
    elif inpt == 'inap':
        try:
            webbrowser.open('voluro.github.io')
            print('app ' + inpt.split()[1] + ' added')
        except:
            print("error code 4 - error in getting app")
    elif inpt == 'listapps':
        for b in allapps:
            print(b)
    else:
        Exception: print("error code 1 - unknown command - invalid syntax")
