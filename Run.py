import os
import sys
import time
import msvcrt
from tkinter.filedialog import askopenfilename

# Menu's
main_menu_file = "main_menu.txt"
play_menu_file = "play_menu.txt"
options_menu_file = "options_menu.txt"
sound_menu_file = "sound_menu.txt"
sound_menu_1_file = "sound_menu_1.txt"
sound_menu_2_file = "sound_menu_2.txt"
sound_menu_3_file = "sound_menu_3.txt"
player_file = "player.txt"

# Game
start_file = "start.txt"




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
            clear_screen()
            print(f.read())
            input("")
            clear_screen()
            

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
start = read_file(start_file)
player = read_file(player_file)

# Game
def game():
    def read_player_sprite():
        with open("player.txt", "r") as file:
            return file.readlines()

    # Set up the screen
    screen_width = 80
    screen_height = 20
    dot_x = screen_width // 2
    dot_speed = 1

    # Load player sprite
    player_sprite = read_player_sprite()

    # Function to draw the player
    def draw_player(dot_x):
        for line in player_sprite:
            print(" " * dot_x + line.strip())

    # Main game loop
    running = True
    while running:
        clear_screen()
        draw_player(dot_x)
        print("Press 'a' to move left, 'd' to move right. Press 'q' to quit.")

        # Handle key presses
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()

            if key == 'a':
                dot_x = max(0, dot_x - dot_speed)
            elif key == 'd':
                dot_x = min(screen_width - 6, dot_x + dot_speed)  # Adjusted for player width
            elif key == 'q':
                running = False

        time.sleep(0.1)  # charactor movement delay

    # Clear the screen before exiting
    clear_screen()



# User save file
save = open("user_data.txt", "w")

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
        elif save_selection == '1':
            clear_screen()
            print("".join(start))
            username = input("Enter a username: ")
            save = open("user_data.txt", "w")  
            save.write("Username: ")
            save.write(username) 
            save.close()  
            game()
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
        if options_selection == '2':
            save.close()
            os.remove("user_data.txt")
                
    elif selection == '3':
        clear_screen()
        break
    else:
        print("Invalid selection. Please try again.")