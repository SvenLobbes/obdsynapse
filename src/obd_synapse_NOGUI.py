# OBD Synapse without graphical user interface

from config.libs import * #import librarys
from display.terminalUI import *
from validateConnection import *
from commands.dataQuery import *


def startDemoView(connection):

    while True:
        currentValues = update_plot_Demo(connection=connection)
        clearDisplay()
        print_DemoUI(currentValues=currentValues)
        time.sleep(0.1)


def main():
    print("[OBD Synapse]: Starting OBD Software")

    print_menu() #startmenu
    connectionType = select_connectionMode()

    #create connection to ECU
    connection = compatibilityConnection(connectionType)
    startDemoView(connection)



if __name__ == "__main__":
    main()
