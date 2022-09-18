def main():

    start = intro()
    board_ttt = grid()
    the_board = grid_board(board_ttt)
    symbol_1, symbol_2 = symbols()
    full = full_board(board_ttt, symbol_1, symbol_2) 
    

    


def intro():

    print("")
    print("Tic Tac Toe!")
    print("")
    print("Rules: \n \nPlayers will be X or O. \n \nTo win match 3 spaces in the grid either vertical, horizontal or diagonal.")
    print("")
    input("Press enter to continue.")
    print("")



def grid():
    print("Let's begin: ")
    board_ttt = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board_ttt




def symbols():
    symbol_1 = input("Player 1, choose X or O: ")
    if symbol_1.upper() == "X":
        symbol_2 = "O"
        print("Player 2, you are O. ")
    else:
        symbol_2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue.")
    print("")
    return (symbol_1, symbol_2)



def startgame(board_ttt, symbol_1, symbol_2, count):


    
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player "+ player +"'s turn. ")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))


    
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        not_in_board(row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

        
    while (board_ttt[row][column] == symbol_1)or (board_ttt[row][column] == symbol_2):
        filled = invalid(board_ttt, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                            "[left column: enter 0, middle column: enter 1, right column enter 2]"))    
        
    
    if player == symbol_1:
        board_ttt[row][column] = symbol_1
            
    else:
        board_ttt[row][column] = symbol_2
    
    return (board_ttt)



def full_board(board_ttt, symbol_1, symbol_2):
    count = 1
    winner = True

    while count < 10 and winner == True:
        gaming = startgame(board_ttt, symbol_1, symbol_2, count)
        nice_board = grid_board(board_ttt)
        
        if count == 9:
            print("The board is full.")
            if winner == True:
                print("It's a tie! ")

        
        winner = win(board_ttt, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over.")
        
    
    report(count, winner, symbol_1, symbol_2)



def not_in_board(row, column):

    print("Innacurate, try again please. ")
    
    

def grid_board(board_ttt):
    rows = len(board_ttt)
    cols = len(board_ttt)
    print("---+---+---")
    for r in range(rows):
        print(board_ttt[r][0], " |", board_ttt[r][1], "|", board_ttt[r][2])
        print("---+---+---")
    return board_ttt



def win(board_ttt, symbol_1, symbol_2, count):

    winner = True
    
    for row in range (0, 3):
        if (board_ttt[row][0] == board_ttt[row][1] == board_ttt[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
   
        elif (board_ttt[row][0] == board_ttt[row][1] == board_ttt[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")
            
            
    
    for col in range (0, 3):
        if (board_ttt[0][col] == board_ttt[1][col] == board_ttt[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board_ttt[0][col] == board_ttt[1][col] == board_ttt[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    
    if board_ttt[0][0] == board_ttt[1][1] == board_ttt[2][2] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + ", you won!")

    elif board_ttt[0][0] == board_ttt[1][1] == board_ttt[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    elif board_ttt[0][2] == board_ttt[1][1] == board_ttt[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")

    elif board_ttt[0][2] == board_ttt[1][1] == board_ttt[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    return winner
    


def invalid(board_ttt, symbol_1, symbol_2, row, column):
    print("Pick another one that has not been used.")
    
    
def report(count, winner, symbol_1, symbol_2):
    print("")
    input("Press enter to see the results. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Winner : Player " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner : Player " + symbol_2 + ".")
    else:
        print("There is a tie. ")

if __name__ == "__main__": main()