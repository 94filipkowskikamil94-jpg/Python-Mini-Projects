
import random


board = list("123456789")

winning_lines = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
]

def display_board():
    print(board[0], "|", board[1], "|", board[2], )
    print("---------")
    print(board[3], "|", board[4], "|", board[5], )
    print("---------")
    print(board[6], "|", board[7], "|", board[8], )


print(" ")
print("Which field do you choose?")
print(" ")

while True:

    print(" ")
    display_board()
    print(" ")
    choice_move = input("1-9: ")
    print(" ")
    index = int(choice_move) - 1 

    if board[index] == "X" or board[index] == "O":

        print(" ")
        print("This square is occupied")
        print(" ")
        continue

    board[index] = "X"

    for line in winning_lines:

        if board[line[0]] == "X" and board[line[1]] == "X" and board[line[2]] == "X":
            print(" ")
            display_board()
            print(" ")
            print("Win!")
            exit()

    while True:  

        drawn = random.randint(0,8)

        if board[drawn] == "X" or board[drawn] == "O":
            continue

        board[drawn] = "O"
        display_board()

        break

    for line in winning_lines:
   
        if board[line[0]] == "O" and board[line[1]] == "O" and board[line[2]] == "O":
            print(" ")
            display_board()
            print(" ")
            print("Lost!")
            exit()
   
