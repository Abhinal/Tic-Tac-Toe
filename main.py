# Board Place
place = {
    1:' ', 2:' ', 3:' ',
    4:' ', 5:' ', 6:' ',
    7:' ', 8:' ', 9:' '
}

# Print Board
def printTable():
    print()
    print(f' {place[1]} | {place[2]} | {place[3]} ')
    print('-----------')
    print(f' {place[4]} | {place[5]} | {place[6]} ')
    print('-----------')
    print(f' {place[7]} | {place[8]} | {place[9]} ')
    print()

# Check if someone wins
def isWin():
    if place[1]==place[2]==place[3]!=' ':
        return True
    if place[4]==place[5]==place[6]!=' ':
        return True
    if place[7]==place[8]==place[9]!=' ':
        return True
    if place[1]==place[4]==place[7]!=' ':
        return True
    if place[2]==place[5]==place[8]!=' ':
        return True
    if place[3]==place[6]==place[9]!=' ':
        return True
    if place[1]==place[5]==place[9]!=' ':
        return True
    if place[3]==place[5]==place[7]!=' ':
        return True

# Check if Draws
def isDraw():
    for i in range(1, 10):
        if place[i]==' ':
            return False
    return True

# Check who will play
def turn(x):
    if x%2:
        return 'O'
    return 'X'

# Take choice
def takeChoice(x):
    number = int(input(f"Player {x%2+1} turn (1-9): "))
    if place[number] == ' ':
        return number
    print()
    print("Invalid Choice! Try Again!")
    print()
    return takeChoice(x)

# Driver Code
if __name__ == "__main__":
    x = 0
    while not isDraw() and not isWin():
        printTable()
        chance = takeChoice(x)
        place[chance] = turn(x)
        x+=1

    if isWin():
        printTable()
        print(f"{turn(x-1)} is winner.")
    else:
        printTable()
        print("Draw!!")