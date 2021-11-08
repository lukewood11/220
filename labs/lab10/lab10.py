"""
Name: <Luke Wood>
<lab10>.py
"""


def build_board():
    position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return position_list


def display_board(position_list):
    print("-" * 10)
    counter = 0
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(position_list[counter], end="|")
            counter = counter + 1
        print()
    print("-" * 10)


def place_spot(position_list, spot, marker):
    position_list[spot -1] = marker


def legal_spot(position_list, spot):
    if (position_list[spot - 1] == "x" or position_list[spot - 1] == "o") or (spot < 1 or spot > 9):
        return False
    else:
        return True


def game_won(position_list):
    winCon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in winCon:
        counter = 0
        for spot in condition:
            if position_list[spot -1] == "x":
                counter += 1
            if counter == 3:
                return "x wins"
        counter = 0
        for spot in condition:
            if position_list[spot -1] == "o":
                counter += 1
            if counter == 3:
                return "o wins"


def game_over(position_list, turnCount):
    if (game_won(position_list) == "x wins" or "o wins") or (turnCount > 9):
        return True
    else:
        return "tie game"


def play_game(position_list):
    display_board(position_list)
    turnCount = 0
    while game_over(position_list, turnCount):
        spot_x = eval(input("select a spot"))
        if legal_spot(position_list, spot_x):
            place_spot(position_list, spot_x, "x")
            display_board(position_list)
        if game_won(position_list) == "x wins":
            print("x wins")
            break
        spot_o = eval(input("select a spot"))
        if legal_spot(position_list, spot_o):
            place_spot(position_list, spot_o, "o")
            display_board(position_list)
        if game_won(position_list) == "o wins":
            print("o wins")
            break
        turnCount = turnCount + 1
    if turnCount == 9:
        print("its tie")


def main():
    # add other function calls here
    position_list = build_board()
    play_game(position_list)
    pass

main()
