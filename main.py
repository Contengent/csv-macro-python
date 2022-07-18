# import modules
import csv
from pynput.mouse import Button, Controller as mouseController      # "as _Controller" is here because only the last module works when
from pynput.keyboard import Key, Controller as keyboardController   # both of them are set to just "Controller".


# apply functions to variables so stuff works and i guess also possible because of ^^^^^^^^^^
mouse = mouseController()
keyboard = keyboardController()


# function for the commands with 3 rows -- and "mouse-press" bc idk what to do with it.
def threeRowFunctions(row):
    match(row[0]): # checking the first row for the command name...
        case "mouse-move":
            print("Moving mouse: {}-x, {}-y".format(row[1],row[2])) # printing out the instruction
            mouse.move(int(row[1]), int(row[2])) # preforming the instruction

        case "mouse-set":
            print("Setting mouse to: {}-x, {}-y".format(row[1],row[2]))
            mouse.position = (int(row[1]), int(row[2]))

        # This one is un-tested bc I'm lazy, and I'm pretty sure it doesn't work lol
            """
        case "mouse-press":
            print("Pressing {} mouse button down...".format(row[1]))
            mouse.press(Button.row[1])
            print("Releasing {} mouse button!".format(row[1]))
            mouse.release(Button.row[1])
            """

# now we have the functions with only two rows
def twoRowFunctions(row):
    match(row[0]): # checking the first row for the command name...
        case "key-down": # commnd name
            print("Pressing {} key down...".format(row[1])) # printing the command to be preformed
            keyboard.press(Key.row[1]) # preforming the command!

        # key-down & key-up don't seem to work, or atleast by themselves? They are untested.
        case "key-up":
            print("Releasing key {}!".format(row[1]))
            keyboard.release(Key.row[1])
        
        case "key-press":
            print("Pressing {} key down...".format(row[1]))
            keyboard.press(Key.row[1])
            print("Releasing key {}!".format(row[1]))
            keyboard.release(Key.row[1])

        case "type-out":
            print("Typing \"{}\"...".format(row[1]))
            keyboard.type(row[1])

        case "mouse-down":
            print("Pressing {} mouse button down...".format(row[1]))
            mouse.press(Button.row[1])

        case "mouse-up":
            print("Releasing {} mouse button!".format(row[1]))
            mouse.release(Button.row[1])



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

# for elegancy
exit() # this line exits the program elegantly.

"""
Edilsteine produmpdinks
 ^-^ |.. |
| ''| v=v
"""