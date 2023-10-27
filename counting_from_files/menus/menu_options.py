from counters.loops_counter import CountLoops as countLoops
from counters.functions_counter import FuncionsCounter as functionCounter
from counters.includes_counter import IncludesCounter as includesCounter
from counters.types_counter import TypesCounter as typesCounter
from utils.fileUtils import FileUtils as fileUtils

counting_type_menu_options = {
    1: "Count loops inside file",
    2: "Count types inside file",
    3: "Create new file with includes inside file",
    4: "Close program",
}

counting_loops_menu_options = {
    1: "Count loops inside file",
    2: "Count functions inside file",
    3: "Go back",
}

counting_types_menu_options = {
    1: "Count int inside file",
    2: "Count void inside file",
    3: "Count float inside file",
    4: "Go back",
}

displayMenu = True
menu_type = 1


class MenuOptions:
    def print_counting_type_menu():
        for key in counting_type_menu_options.keys():
            print(key, "--", counting_type_menu_options[key])

    def print_counting_loops_menu():
        for key in counting_loops_menu_options.keys():
            print(key, "--", counting_loops_menu_options[key])

    def print_counting_types_menu():
        for key in counting_types_menu_options.keys():
            print(key, "--", counting_types_menu_options[key])

    def openFileFromPath():
        return fileUtils.openFile()

    # Check what choice was entered and act accordingly
    while displayMenu:
        option = ""
        match menu_type:
            case 1:
                print_counting_type_menu()
                try:
                    option = int(input("Enter your choice: "))
                except:
                    print("Wrong input. Please enter a number ...")
                # Check user choice and act accordingly
                if option == 1:
                    menu_type = 2
                elif option == 2:
                    menu_type = 3
                elif option == 3:
                    fileUtils.safeToFile(
                        includesCounter.listOfIncludesInFile(openFileFromPath()),
                        "D:\PythonTraining\includes.txt",
                    )
                elif option == 4:
                    print("Program closed")
                    exit()
                else:
                    print("Invalid option. Please enter a number between 1 and 4.")
            case 2:
                print_counting_loops_menu()
                try:
                    option = int(input("Enter your choice: "))
                except:
                    print("Wrong input. Please enter a number ...")
                # Check user choice and act accordingly
                if option == 1:
                    countLoops.countLoops(openFileFromPath())
                elif option == 2:
                    functionCounter.countFunctions(openFileFromPath())
                elif option == 3:
                    menu_type = 1
                else:
                    print("Invalid option. Please enter a number between 1 and 4.")
            case 3:
                print_counting_types_menu()
                try:
                    option = int(input("Enter your choice: "))
                except:
                    print("Wrong input. Please enter a number ...")
                # Check user choice and act accordingly
                if option == 1:
                    typesCounter.countIntTypes(openFileFromPath())
                elif option == 2:
                    typesCounter.countVoidTypes(openFileFromPath())
                elif option == 3:
                    typesCounter.countFloatTypes(openFileFromPath())
                elif option == 4:
                    menu_type = 1
                else:
                    print("Invalid option. Please enter a number between 1 and 4.")
