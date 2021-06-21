import functions
from functions import *

# main function
if __name__ == '__main__':
    while True:
        set_default()
        change_player_mark()
        print_start_screen()
        while not functions.game_over:
            if functions.player_mark == "X":
                print_playground()
                player_input()
                if functions.game_over:
                    break
                computer_input()
            else:
                computer_input()
                if functions.game_over:
                    break
                print_playground()
                player_input()
        play_again_input = ""
        while not (play_again_input == "y" or play_again_input == "n") :
            play_again_input = input("Do you want to play again? Type in Y or N: ")
            play_again_input = play_again_input.lower()
        if play_again_input == "n":
            break
        else:
            clear()
    x = input("Bye bye!")


