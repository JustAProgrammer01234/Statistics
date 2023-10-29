import os 

from grouped_data import main_grouped_data
from ungrouped_data import main_ungrouped_data 

def input_options(section):
    if section == "mm":
        print("A] Visualize (Coming soon!)")
        print("B] Calculate")
    else:
        print("A] Ungrouped Data")
        print("B] Grouped Data")
    
    print("C] Show input options")
    print()

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def choose_calculation():
    print("Would you like to calculate grouped or ungrouped data? (Use the letter behind ']')")

    right_answers = ['A', 'B']

    letter = None 
    
    while True:
        letter = input("[Calculate Section] Choose your letter (press q to exit to main menu): ").strip()

        match letter:
            case 'q':
                clear_terminal()
                break 
            case 'A':
                print()
                main_ungrouped_data()
            case 'B':
                print()
                main_grouped_data()

if __name__ == "__main__":
    right_answers = ['A', 'B']

    letter = None 

    print("Welcome to Statistics! A program that makes use of various methods in statistics to calculate and visualize data!")
    print("Note that the data are located in the data folder in the directory this python file is in.\n")
    print("Would you like to visualize or calculate data? (Use the letter behind ']')")
    input_options("mm")

    while True:

        letter = input("[Main Menu] Choose your letter (press q to quit): ").strip()
        
        if letter not in right_answers:
            print("Wrong input!")
    
        match letter:
            case 'q':
                exit()
            case 'A':
                print("This is currently in development!")
            case 'B':
                clear_terminal()
                choose_calculation()
            case 'C':
                input_options("mn")