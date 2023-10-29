import os 

from calculation.grouped_data import main_grouped_data
from calculation.ungrouped_data import main_ungrouped_data 

from visualization.grouped_data import * 
from visualization.ungrouped_data import * 

def input_options(section = None):
    print()

    if section == "mm":
        print("A] Visualize")
        print("B] Calculate")
    elif section == "v":
        print("A] Line Graph")
        print("B] Bar Graph")
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

def clear_the_screen():
    while True:
        letter = input("Would you like to go back? (Enter Y if you want.): ").strip()

        if letter == "Y":
            clear_terminal()
            break 

    print("Would you like to calculate grouped or ungrouped data? (Use the letter behind ']')")
    input_options()

def choose_calculation():
    print("Would you like to calculate grouped or ungrouped data? (Use the letter behind ']')")
    input_options()

    letter = None 
    
    while True:
        letter = input("[Calculate Section] Choose your letter (press q to exit to the main menu): ").strip()

        match letter:
            case 'q':
                clear_terminal()
                print("Welcome back to the main menu! ")
                print("Note that the data are located in the data folder in the directory this python file is in.\n")
                print("Would you like to visualize or calculate data? (Use the letter behind ']')")
                input_options(section = "mm")
                break 
            case 'A':
                clear_terminal()
                main_ungrouped_data()
                print()
                clear_the_screen()
            case 'B':
                clear_terminal()
                main_grouped_data()
                print()
                clear_the_screen()
            case 'C':
                input_options()

def choose_visualization(is_grouped):
    print("Would you like to choose Line or Bar graph? (Use the letter behind ']')")
    input_options(section = "v")

    indicator = "Grouped Data" if is_grouped else "Ungrouped Data"

    if is_grouped:
        line_graph = line_graph_grouped
        bar_graph = bar_graph_grouped
    else:
        line_graph = line_graph_ungrouped
        bar_graph = bar_graph_ungrouped

    while True:
        letter = input(f"[Visualize {indicator} Section] Choose your letter (press q to exit to main menu): ")

        match letter:
            case 'q':
                clear_terminal()
                print("Would you like to visualize grouped or ungrouped data? (Use the letter behind ']')")
                input_options(section = "v")
                break 
            case 'A':
                line_graph() 
            case 'B':
                bar_graph() 
            case 'C':
                input_options()

def choose_data_visualization():
    print("Would you like to visualize grouped or ungrouped data? (Use the letter behind ])")
    input_options()

    while True:
        letter = input("[Visualize Section] Choose your letter (press q to exit to main menu): ").strip()

        match letter:
            case 'q':
                clear_terminal()
                print("Welcome back to the main menu! ")
                print("Note that the data are located in the data folder in the directory this python file is in.\n")
                print("Would you like to visualize or calculate data? (Use the letter behind ']')")
                input_options(section = "mm")
                break 
            case 'A':
                clear_terminal()
                choose_visualization(False)
            case 'B':
                clear_terminal()
                choose_visualization(True)
            case 'C':
                input_options()

if __name__ == "__main__":
    letter = None 

    clear_terminal()
    print("Welcome to Statistics! A program that makes use of various methods in statistics to calculate and visualize data!")
    print("Note that the data are located in the data folder in the directory this python file is in.\n")
    print("Would you like to visualize or calculate data? (Use the letter behind ']')")
    input_options("mm")

    while True:

        letter = input("[Main Menu] Choose your letter (press q to quit): ").strip()
    
        match letter:
            case 'q':
                exit()
            case 'A':
                clear_terminal()
                choose_data_visualization()
            case 'B':
                clear_terminal()
                choose_calculation()
            case 'C':
                input_options("mn")