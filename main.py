def sum(a,b,c):
    return a+b+c

def printBoard(xState,yState):
    # for i in range(0,8):
    #     print(f"{'X' if xState[i] else ('O' if yState[i] else ' ')}",end=" ")
    #     if i==2 or i==5 :
    #         print()
    zero =  'X' if xState[0] else ('O' if yState[0] else " ")
    one =  'X' if xState[1] else ('O' if yState[1] else " ")
    two =  'X' if xState[2] else ('O' if yState[2] else " ")
    three =  'X' if xState[3] else ('O' if yState[3] else " ")
    four =  'X' if xState[4] else ('O' if yState[4] else " ")
    five =  'X' if xState[5] else ('O' if yState[5] else " ")
    six =  'X' if xState[6] else ('O' if yState[6] else " ")
    seven = 'X' if xState[7] else ('O' if yState[7] else " ")
    eight =  'X' if xState[8] else ('O' if yState[8] else " ")

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
    
def checkWin(xState, yState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[1,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if sum(xState[win[0]],xState[win[1]],xState[win[2]]) == 3:
            print("X is the winner !!")
            return 1
        if sum(yState[win[0]],yState[win[1]],yState[win[2]]) == 3:
            print("O is the Winner !!")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 #1 for X and 0 for O
    print("Welcome to Tic Tac Toe !!!")
    while(True):
        if (turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value"))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value"))
            yState[value] = 1

        ans = checkWin(xState, yState)
        printBoard(xState,yState)
        if ans != -1:
            print("MATCH OVER")
            break
        turn = 1-turn