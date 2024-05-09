import os
import sys
import time
import msvcrt
from tkinter.filedialog import askopenfilename


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
        print("File {filename} not found.")
        return []
    except Exception as e:
        print("An error occurred: {e}")
        return []

# Read main menu and play_menu
main_menu_file = "main_menu.txt"
play_menu_file = "play_menu.txt"
options_menu_file = "options_menu.txt"
sound_menu_file = "sound_menu.txt"
sound_menu_1_file = "sound_menu_1.txt"
sound_menu_2_file = "sound_menu_2.txt"
sound_menu_3_file = "sound_menu_3.txt"
start_file = "start.txt"
tree_file = "tree.txt"
player_file = "player.txt"
box_entity_file = "box_entity.txt"
hole_file = "hole.txt"

# Goblin
goblin_file = "goblin.txt"
goblin_0_file = "goblin_0.txt"
goblin_1_file = "goblin_1.txt"
goblin_2_file = "goblin_2.txt"
goblin_3_file = "goblin_3.txt"
goblin_4_file = "goblin_4.txt"
goblin_5_file = "goblin_5.txt"
goblin_6_file = "goblin_6.txt"
goblin_7_file = "goblin_7.txt"
goblin_8_file = "goblin_8.txt"
goblin_9_file = "goblin_9.txt"
goblin_10_file = "goblin_10.txt"
goblin_11_file = "goblin_11.txt"

goblin_0_0_file = "goblin_0_0.txt"
goblin_0_1_file = "goblin_0_1.txt"
goblin_0_2_file = "goblin_0_2.txt"

goblin = read_file(goblin_file)
goblin_0 = read_file(goblin_0_file)
goblin_1 = read_file(goblin_1_file)
goblin_2 = read_file(goblin_2_file)
goblin_3 = read_file(goblin_3_file)
goblin_4 = read_file(goblin_4_file)
goblin_5 = read_file(goblin_5_file)
goblin_6 = read_file(goblin_6_file)
goblin_7 = read_file(goblin_7_file)
goblin_8 = read_file(goblin_8_file)
goblin_9 = read_file(goblin_9_file)
goblin_10 = read_file(goblin_10_file)
goblin_11 = read_file(goblin_11_file)

goblin_0_0 = read_file(goblin_0_0_file)
goblin_0_1 = read_file(goblin_0_1_file)
goblin_0_2 = read_file(goblin_0_2_file)

main_menu = read_file(main_menu_file)
play_menu = read_file(play_menu_file)
options_menu = read_file(options_menu_file)

sound_menu = read_file(sound_menu_file)
sound_menu_temp = read_file(sound_menu_file)
sound_menu_1 = read_file(sound_menu_1_file)
sound_menu_2 = read_file(sound_menu_2_file)
sound_menu_3 = read_file(sound_menu_3_file)

start = read_file(start_file)
tree = read_file(tree_file)
box = read_file(box_entity_file)
hole = read_file(hole_file)





def game():
    def draw_player(dot_x, player_sprite):
        tree_height = len(tree)
        player_y = screen_height - tree_height - len(player_sprite)
        for i, line in enumerate(player_sprite):
            print(" " * dot_x + " " * (tree_height) + line.strip())

    def read_player_sprites():
        # Read all player sprites
        player_sprites = []
        for i in range(1, 11):
            with open(f"player_{i}.txt", "r", encoding="utf-8") as file:
                player_sprites.append(file.readlines())
        return player_sprites

    def draw_hole():
        tree_height = len(tree)
        hole_y = screen_height - tree_height - 1
        print(" " * (screen_width - 1) + "O")

    # Set up the screen
    screen_width = 80
    screen_height = 20
    dot_x = screen_width // 2
    dot_speed = 1

    # Load player sprites
    player_sprites = read_player_sprites()
    num_frames = len(player_sprites)
    current_frame = 0

    # Main game loop
    running = True
    while running:
        clear_screen()
        print("".join(tree))  # Print the tree first
        draw_player(dot_x, player_sprites[current_frame])  # Draw the player sprite
        draw_hole()  # Draw the hole

        # Move to the next frame for animation
        current_frame = (current_frame + 1) % num_frames
        print("Press 'a' to move left, 'd' to move right. Press 'q' to quit.")

        # Handle key presses
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()

            if key == 'a':
                dot_x = (dot_x - dot_speed) % screen_width  # Wrap around to the other side
            elif key == 'd':
                dot_x = (dot_x + dot_speed) % screen_width  # Wrap around to the other side
            elif key == 'q':
                running = False

        # Check if player is above the hole
        if dot_x == (screen_width - 12):
            clear_screen()
            print("Enter 'yes' or 'no'")
            enter = input("Would you like to begin the game?")
            if enter == "yes":
                timevar = 0.05
                clear_screen()
                print("".join(goblin_0))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_1))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_2))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_3))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_4))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_5))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_6))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_7))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_8))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_9))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_10))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin_11))
                time.sleep(timevar)
                clear_screen()
                print("".join(goblin))
                input("Press enter to continue:")
                clear_screen()
                print("".join(goblin_0_0))
                input("Press enter to continue:")
                clear_screen()
                print("".join(goblin_0_1))
                input("Press enter to continue:")
                clear_screen()
                print("".join(goblin_0_2))
                username = input("Enter a username: ")
                save = open("user_data.txt", "w")
                save.write("Username: ")
                save.write(username)
                save.close()
            return

        time.sleep(0.1)  # character movement delay


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
