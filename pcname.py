import savedsettings as sdss
def pcname():
    impy = input("please enter your new pc name:")
    sdss.save('pcname', impy)