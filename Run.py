import os
from tkinter.filedialog import askopenfilename

# Menu's
main_menu_file = "main_menu.txt"
play_menu_file = "play_menu.txt"
options_menu_file = "options_menu.txt"
sound_menu_file = "sound_menu.txt"
sound_menu_1_file = "sound_menu_1.txt"
sound_menu_2_file = "sound_menu_2.txt"
sound_menu_3_file = "sound_menu_3.txt"

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to open files
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filepath:
        with open(filepath, "r", encoding="utf8") as f:
            print(f.read())

# Function to read from a file and return its content
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf8") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Read main menu and play_menu
main_menu = read_file(main_menu_file)
play_menu = read_file(play_menu_file)
options_menu = read_file(options_menu_file)
sound_menu = read_file(sound_menu_file)
sound_menu_temp = read_file(sound_menu_file)
sound_menu_1 = read_file(sound_menu_1_file)
sound_menu_2 = read_file(sound_menu_2_file)
sound_menu_3 = read_file(sound_menu_3_file)

while True:
    clear_screen()
    print("".join(main_menu))
    selection = input("Selection: ")
    
    if selection == '1':
        clear_screen()
        print("".join(play_menu))
        save_selection = input("Selection: ")
        if save_selection == '2':
            open_file()
    elif selection == '2':
        clear_screen()
        print("".join(options_menu))  
        options_selection = input("Selection: ")
        if options_selection == "1":
            clear_screen()
            print("".join(sound_menu))
            sound_selection = input("Enter a value between 0-3: ")
            if sound_selection == "0":
                sound_menu = sound_menu_temp
                clear_screen()
                print("".join(sound_menu))
                sound_selection = input("Enter a value between 0-3: ")
                
            elif sound_selection == "1":
                sound_menu = sound_menu_1
                clear_screen()
                print("".join(sound_menu_1))
                sound_selection = input("Enter a value between 0-3: ")
                
            elif sound_selection == "2":
                sound_menu = sound_menu_2
                clear_screen()
                print("".join(sound_menu_2))
                sound_selection = input("Enter a value between 0-3: ")
            elif sound_selection == "3":
                sound_menu = sound_menu_3
                clear_screen()
                print("".join(sound_menu_3))
                sound_selection = input("Enter a value between 0-3: ")
    elif selection == '3':
        clear_screen()
        break
    else:
        print("Invalid selection. Please try again.")