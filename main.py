from functions import *

# main function
if __name__ == '__main__':
    change_player_mark()
    print_start_screen()
    while not game_over:
        if player_mark == "X":
            print_playground()
            player_input()
            if game_over:
                break
            computer_input()
        else:
            computer_input()
            if game_over:
                break
            print_playground()
            player_input()




