#########################################
#                                       #
#       ToDoApp - To-do-list            #
#                                       #
#########################################

### Define imports here
import json
### Define global variables here
listOfDictionaries = []                                 # List of dictionaries
filename = "Harjoitustyö\database.json"                 # Path name of the JSON -file
### Define functions here
def loadNotes():
    # Load notes from a JSON-file function
    # JSON -file is array of objects ==>> in Python it is list of dictionaries
    # Read the file
    with open(filename, 'r') as data_file:
        json_data = data_file.read()
    # 'data' becames a list and each JSON object will be a dictionary
    data = json.loads(json_data)
    # Return a list of dictionaries
    return data

def printSelection(char):
    # Print selection function
    # prints depending what user inputs
    if char == 'e' or char == 'E':
        return "You chose to Exit the application. Good bye!\n"
    elif char == 'r' or char == 'R':
        return "You chose to Read notes.\n"
    elif char == 'd' or char == 'D':
        return "You chose to Delete notes.\n"
    elif char == 'w' or char == 'W':
        return "You chose to Write a new note.\n"
    else:
        return "Not a valid input.\n"

def readNotes():
    # Read notes -function
    # Load notes from a file
    listOfDictionaries = loadNotes()
    # If not null
    if len(listOfDictionaries) > 0:
        # Create a header text as a String
        headerText = "id |"+" Done" + "  | Note"
        # Print the header
        print(headerText)
        # Create just a String of "-"
        dashText = "-" * len(headerText)
        # Print the dash
        print(dashText)
        # Print all items from the list of dictionaries as a nice list
        for x in range(len(listOfDictionaries)):
            print( str(x) + "  | " +  listOfDictionaries[x]['done'] + " | " + listOfDictionaries[x]['name'] )
        # Print some feedback text
        print("All notes read from a file.\n")
    else:
        print("There is nothing to print!\n")

def writeNotes():
    # Write a new note -function
    # Load notes from a file
    listOfDictionaries = loadNotes()
    # create new dictionary item 
    note_dict = {"name": "", "done": ""}                # Define a dictionary with two items
    isNameNull = True                                   # Define a help variable
    while isNameNull == True:
        # User input for a name for the note
        noteName = input("Give a name for a new note: ")
        #Check wether the input is null or not
        if noteName:
            isNameNull = False
        else:
            print("Do not give empty name for a note!\n")
    # Write items to the dictionary
    note_dict["name"] = noteName
    note_dict["done"] = "False"
    # add new dictionary item to a 'data'-list
    listOfDictionaries.append(note_dict)
    # save updated list of dictionaries to a JSON-file as an array of objects
    with open(filename, 'w') as fout:
        json.dump(listOfDictionaries , fout)
    # Print some feedback text
    print("New note saved to a file.\n")

def deleteNotes():
    # Delete notes -function
    # Loads notes from a JSON file, prints the list, asks what to be deleted and saves a updated list to a JSON-file
    isInputValid = False                                   # Define a help variable
    # Load notes from a file
    listOfDictionaries = loadNotes()
    # If not null
    if len(listOfDictionaries) > 0:
        # Create a header text as a String
        headerText = "id |"+" Done" + "  | Note"
        # Print the header
        print(headerText)
        # Create just a String of "-"
        dashText = "-" * len(headerText)
        # Print the dash
        print(dashText)
        # Print all items from the list of dictionaries as a nice list
        for x in range(len(listOfDictionaries)):
            print( str(x) + "  | " +  listOfDictionaries[x]['done'] + " | " + listOfDictionaries[x]['name'] )
        print("")
        while isInputValid == False:
            # User input for a index number
            deleteId = input("Give a note number to be deleted: ")
            try:
                # Check if input is a integer
                val = int(deleteId)

                # if value is integer, check if it is valid regarding to a list 
                if val > (len(listOfDictionaries)-1):
                    print("Value is too high!\n")
                elif val < 0:
                    print("Value is too small!\n")
                else:
                    isInputValid = True
            except ValueError:
                print("That's not an int!\n")

        # Delete selected id from a list of dictionaries
        listOfDictionaries.pop(int(deleteId))
        # save updated list of dictionaries to a JSON-file as an array of objects
        with open(filename, 'w') as fout:
            json.dump(listOfDictionaries , fout)
        # Print some feedback text
        print("")
        print("Note deleted.\n")
    else:
        print("There is nothing to delete.\n")

# Start application here and print a cool logo
print("")
print("""
///////////////          ////////
///////////////          //     //
      //                 //      //
      //                 //       //
      //    OOOOO        //       //   OOOOO
      //   OO   OO       //       //  OO   OO
      //  OO     OO //// //      //  OO     OO
      //   OO   OO       //     //    OO   OO
      //    OOOOO        ////////      OOOOO

                        To-Do-List APPLICATION""")
print("")
while True:
    # ask user what to do and print the selection
    input1 = input("What to do?\n   (R)ead notes.\n   (W)rite a new note.\n   (D)elete a note.\n   (E)xit.\n")
    print("")
    print(printSelection(input1))
    # Choose where to go next in this program
    if input1 == 'e' or input1 == 'E':
        break
    elif input1 == 'r' or input1 == 'R':
        readNotes()
    elif input1 == 'd' or input1 == 'D':
        deleteNotes()
    elif input1 == 'w' or input1 == 'W':
        writeNotes()
    else:
        continue