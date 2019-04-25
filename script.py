board = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

game_over = False
while not game_over:
    valid_p1_move = False
    while not valid_p1_move:
        print(f"""----------
| {board[1]} | {board[2]} | {board[3]} |
----------
| {board[4]} | {board[5]} | {board[6]} |
----------
| {board[7]} | {board[8]} | {board[9]} |
----------
""")
        try:
            p1_move = int(input("Player 1, choose your space: "))
            if 1 <= p1_move <= 9:
                if board[p1_move] == "":
                    valid_p1_move = True
                    board[p1_move] = "X"
                else:
                    print("Space is taken.\n")
            else:
                print("Invalid space.\n")
        except ValueError:
            print("Invalid space.\n")
    valid_p2_move = False
    while not valid_p2_move:
        print(f"""----------
| {board[1]} | {board[2]} | {board[3]} |
----------
| {board[4]} | {board[5]} | {board[6]} |
----------
| {board[7]} | {board[8]} | {board[9]} |
----------
""")
        try:
            p2_move = int(input("Player 2, choose your space: "))
            if 1 <= p2_move <= 9:
                if board[p2_move] == "":
                    valid_p2_move = True
                    board[p2_move] = "O"
                else:
                    print("Space is taken.\n")
            else:
                print("Invalid space.\n")
        except ValueError:
            print("Invalid space.\n")
