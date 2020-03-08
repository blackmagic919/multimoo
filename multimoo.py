def getFirstParent(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != '_':
                return (column, row)

def floodfillMatrix(M, x, y, region, count):
    M[y][x] = '_'
    count += 1

    if x > 0:
        if M[y][x-1] == region:
            count = floodfillMatrix(M, x-1, y, region, count)
    if x < len(M[y])-1:
        if M[y][x+1] == region:
            count = floodfillMatrix(M, x+1, y, region, count)
    if y > 0:
        if M[y-1][x] == region:
            count = floodfillMatrix(M, x, y-1, region, count)
    if y < len(M)-1:
        if M[y+1][x] == region:
            count = floodfillMatrix(M, x, y+1, region, count)
    return count

with open("multimoo.in") as fInput:
    lines = fInput.readlines()
N = int(lines[0].strip())
board = [[int(n) for n in lines[i].strip().split()] for i in range(1, N+1)]

sol = 0

while getFirstParent(board) != None:
    x, y = getFirstParent(board)
    check = 0
    sol = max(sol, floodfillMatrix(board, x, y, board[y][x], 0))

1==1
