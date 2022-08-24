# SHOUT OUTS TO FUCKING NOBODY, WHY DOES WIN32API LETTER KEYS NOT WORK IN ADMIN PROCESSES?!?!?!??!?!
# i need to rebuild this entire project in something like c++, idk i might shoot myself?
# import modules
import csv
import time
import win32api, win32con
from pynput.mouse import Button, Controller as mouseController      # "as _Controller" is here because only the last module works when
from pynput.keyboard import Key, Controller as keyboardController   # both of them are set to just "Controller".


# apply functions to variables so stuff works and i guess also possible because of ^^^^^^^^^^
mouse = mouseController()
keyboard = keyboardController()


# key dictoniantry bc it has to be streamliened
DickToneAery = {
    "left":  0x25,
    "up":    0x26,
    "right": 0x27,
    "down":  0x28,

    "ctrl":  0x11
}

def keyPressDown(keyValue):
    win32api.keybd_event(keyValue, 0, 0, 0) # key-press event(key-hex, idk, press, idk)
def keyReleaseUp(keyValue):
    win32api.keybd_event(keyValue, 0, win32con.KEYEVENTF_KEYUP, 0)  # key-release event(key-hex, ?, release, ??)


# function for the commands with 3 rows -- and "mouse-press" bc idk what to do with it.
def threeRowFunctions(row):
    match(row[0]): # checking the first row for the command name...
        case "mouse-move":
            print("Moving mouse: {}-x, {}-y".format(row[1],row[2])) # printing out the instruction
            mouse.move(int(row[1]), int(row[2])) # preforming the instruction

        case "mouse-set":
            print("Setting mouse to: {}-x, {}-y".format(row[1],row[2]))
            mouse.position = (int(row[1]), int(row[2]))

        
            

# now we have the functions with only two rows
def twoRowFunctions(row):
    match(row[0]): # checking the first row for the command name...
        case "key-down": # commnd name
            if len(row[1]) > 1:
                print("Pressing {} key down...".format(row[1])) # printing the command to be preformed
                keyPressDown(DickToneAery[row[1]])  # preforming the command!
                print("don-oh")
            else:
                print("Pressing {} key down...".format(row[1])) # printing the command to be preformed
                keyboard.press(row[1]) # preforming the command
                print("works?")

        # key-down & key-up don't seem to work, or atleast by themselves? They are untested.
        case "key-up":
            if len(row[1]) > 1:
                print("Pressing {} key down...".format(row[1])) # printing the command to be preformed
                keyReleaseUp(DickToneAery[row[1]])  # preforming the command!
                print("don-oh")
            else:
                print("Pressing {} key down...".format(row[1])) # printing the command to be preformed
                keyboard.release(row[1]) # preforming the command
                print("works?")
        
        case "key-press":
            if len(row[1]) > 1:
                print("Pressing {} key down...".format(row[1])) # printing the command to be preformed
                keyPressDown(DickToneAery[row[1]])  # preforming the command!
                print("releasing key")
                keyReleaseUp(DickToneAery[row[1]])
                print("don")
            else:
                print("Pressing {} key down...".format(row[1]))
                keyboard.press(row[1])
                print("Releasing key {}!".format(row[1]))
                keyboard.release(row[1])
                print("don")

        case "type-out":
            print("Typing \"{}\"...".format(row[1]))
            keyboard.type(row[1])

        # IT WORKS NOW! but idk if it's efficent or na, I also fixed the other mouse presses :l
        case "mouse-down":
            if(row[1] == "left"):
                print("Pressing left mouse button down...")
                mouse.press(Button.left)
            if(row[1] == "right"):
                print("Pressing right mouse button down...")
                mouse.press(Button.right)

        case "mouse-up":
            if(row[1] == "left"):
                print("Releasing left mouse button!")
                mouse.release(Button.left)
            if(row[1] == "right"):
                print("Releasing right mouse button!")
                mouse.release(Button.right)
            
        case "mouse-press":
            if(row[1] == "left"):
                print("Pressing left mouse button down...")
                mouse.press(Button.left)
                print("Releasing left mouse button!")
                mouse.release(Button.left)
            if(row[1] == "right"):
                print("Pressing right mouse button down...")
                mouse.press(Button.right)
                print("Releasing right mouse button!")
                mouse.release(Button.right)
        
        case "sleep":
            print("sleeping...")
            time.sleep(int(row[1]))
            print("awake!")



# The 'compilation function,' if you will
def readCsvFile(selected_csv):
    # file selection
    with open(selected_csv) as csv_file:
        # pass file name and row seperator
        csv_reader = csv.reader(csv_file, delimiter=' ')

        # setting variable 'line_count' to determine what line to read
        line_count = 0

        # loop for the amount of rows in "csv_reader"
        for row in csv_reader:
            # check if the instruction has 2 or 3 columns to seperate them. More efficient then just trying them all I guess :L
            try:
                print(row[0], row[1], row[2])
                threeRowFunctions(row)
            # exception for the commands with 2 rows
            except:
                print(row[0], row[1])
                twoRowFunctions(row)
            
            # Increment counter
            line_count += 1

# main function
def main():
    # Input filter(?)
    while(True):
        try:
            # get file input from user
            selection = input("Select a file to read or type \"exit\": ")
            
            # allow "exit" to exit the program
            if(selection == "exit"):
                print("exiting...")
                break
            # start the main function of the program!
            else:
                readCsvFile(selection)  #/* I should add a new check for if the commands were entered incorrectly or smth idk /*#
                print("Done!\n")
                
        # except when the input from user is not valid
        except:
            print("error! your input is invalid.\n")

main()

# for elegancy
exit() # this line exits the program elegantly.

"""
Edilsteine produmpdinks
 ^-^ |.. |
| ''| v=v
"""