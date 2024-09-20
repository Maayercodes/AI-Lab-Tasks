if __name__ == "__main__":
    size = int(input("Enter the size of the Tic Tac Toe board (e.g., 3 for 3x3): "))
    xState = [0] * (size * size)
    zState = [0] * (size * size)
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    
    while True:
        printBoard=(xState, zState, size)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1
        
        cwin = checkWin(xState, zState, size) # Ensure cwin is assigned here

        if cwin != -1:  # Correct comparison operator
            printBoard(xState, zState, size)
            print("Match over")
            break

        turn = 1 - turn  # Switch turn
