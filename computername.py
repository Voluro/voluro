import savedsettings as sdss
def computername():
    impy = input("please enter your new computer name:")
    sdss.save('computername', impy)
    exit("new computername set")
