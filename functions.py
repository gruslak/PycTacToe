import random

player_mark = ""
computer_mark = ""
playground_content = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
game_over = False;


# prints the start screen
def print_start_screen():
    print('Welcome to my console-based game of Tic Tac Toe!')
    print('Your mark is the "' + player_mark + '".')
    print('Type in a number to draw a mark at the numbers square.')


# prints the playground
def print_playground():
    print(' _______   _______   _______')
    print('|       | |       | |       |')
    print('|   ' + playground_content[0] + '   | |   ' + playground_content[1] + '   | |   ' + playground_content[
        2] + '   |')
    print('|___1___| |___2___| |___3___|')
    print(' _______   _______   _______')
    print('|       | |       | |       |')
    print('|   ' + playground_content[3] + '   | |   ' + playground_content[4] + '   | |   ' + playground_content[
        5] + '   |')
    print('|___4___| |___5___| |___6___|')
    print(' _______   _______   _______')
    print('|       | |       | |       |')
    print('|   ' + playground_content[6] + '   | |   ' + playground_content[7] + '   | |   ' + playground_content[
        8] + '   |')
    print('|___7___| |___8___| |___9___|')


# changes the team-mark of the player
def change_player_mark():
    global player_mark
    global computer_mark

    n = random.randint(0, 1)
    if n > 0:
        player_mark = "X"
        computer_mark = "O"
    else:
        player_mark = "O"
        computer_mark = "X"


# player-input algorithm
def player_input():
    print("Your turn.")
    while True:
        user_input = input("type in a number: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            user_input -= 1
            if is_valid_number(user_input):
                playground_content[user_input] = player_mark
                game_over_checker()
                break
            else:
                print("Your input is not a valid number. Try again!")


# computer-input algorithm
def computer_input():
    print("Computers turn.")
    while True:
        n = random.randint(0, 8)
        if is_valid_number(n):
            playground_content[n] = computer_mark
            game_over_checker()
            break


# bool: if a number is a valid position in this projects context
def is_valid_number(n):
    if n < 0 or n > 8:
        return False
    elif not str.isspace(playground_content[n]):
        return False
    else:
        return True


# defines game_over variables value
# checks all game over conditions
# prints game over message
def game_over_checker():
    global game_over

    vertical_check = [3, 4, 5]
    horizontal_check = [1, 4, 7]
    diagonal_downwards_check = 0
    diagonal_upwards_check = 6

    winning_mark = ""

    #vertical
    for n in vertical_check:
        if not playground_content[n].isspace():
            if playground_content[n] == playground_content[n-3] == playground_content[n+3]:
                game_over = True
                winning_mark = playground_content[n]
                break
    #horizontal
    for n in horizontal_check:
        if not playground_content[n].isspace():
            if playground_content[n] == playground_content[n+1] == playground_content[n-1]:
                game_over = True
                winning_mark = playground_content[n]
                break
    #diagonal_downwards
    n = diagonal_downwards_check
    if not playground_content[n].isspace():
        if playground_content[n] == playground_content[n+4] == playground_content[n+8]:
            game_over = True
            winning_mark = playground_content[n]
    # diagonal_upwards
    n = diagonal_upwards_check
    if not playground_content[n].isspace():
        if playground_content[n] == playground_content[n - 2] == playground_content[n - 4]:
            game_over = True
            winning_mark = playground_content[n]

    # check if any game_over condition occurs
    if game_over:
        if winning_mark == player_mark:
            print_playground()
            print("Congratulations! You win.")
        else:
            print_playground()
            print("Game over! You loose.")
    # check if its a draw
    else:
        draw_condition = True
        for m in playground_content:
            if m.isspace():
                draw_condition = False
                break
        if draw_condition:
            game_over = True
            print_playground()
            print("Game over! Its a draw.")