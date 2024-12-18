def doesLineExist(i, j, increment, side, board, visited, letter, vert):

    
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    if board[i][j] != letter:
        return False
    
    match side:
        case 0:
            if i > 0:
                if board[i-1][j] != letter:
                    if visited[i][j]:
                        
                        return True
                else:
                    return False
            else:
                if visited[i][j]:
                    return True
        case 1:
            if j > 0:
                if board[i][j-1] != letter:
                    if visited[i][j]:
                        return True
                else:
                    return False
            else:
                if visited[i][j]:
                    return True
        case 2:
            if i < len(board) - 1:
                if board[i+1][j] != letter:
                    if visited[i][j]:
                        return True
                else:
                    return False
            else:
                
                if visited[i][j]:
                    return True
        case 3:

            if j < len(board[0]) -1:
                if board[i][j + 1] != letter:

                    if visited[i][j]:
                        
                        return True
                else:
                    return False
            else:
                if visited[i][j]:
                    return True
    if vert:
        return doesLineExist(i + increment, j, increment, side, board, visited, letter, True)
    
    return doesLineExist(i, j + increment, increment, side, board, visited, letter, False)
    

def checkTile(i, j, board, side, letter):
    
    match side:
        case 0:
            if i > 0:
                if board[i-1][j] == letter:
                    return False
            return True
        case 1:
            if j > 0:
                if board[i][j-1] == letter:
                    return False
            return True
        case 2:
            if i < len(board)-1:
                if board[i+1][j] == letter:
                    return False
            return True
        case 3:
            if j < len(board[0]) - 1:
                if board[i][j+1] == letter:
                    return False
            return True
        
def recur(i, j, board, visited, letter, previous) -> tuple[int]:

    y, x = previous
    area, per = 1, 0

    visited[i][j] = True
    if checkTile(i, j, board, 0, letter):
        topLeftCheck  = doesLineExist(i, j-1, -1, 0, board, visited, letter, False)
        topRightCheck = doesLineExist(i, j+1, +1, 0, board, visited, letter, False)  
        per += 1 if not topLeftCheck and not  topRightCheck else 0
    
    if checkTile(i, j, board, 2, letter):
        bottomLeftCheck  = doesLineExist(i, j-1, -1, 2, board, visited, letter, False)
        bottomRightCheck = doesLineExist(i, j+1, +1, 2, board, visited, letter, False)  
        
        per += 1 if not bottomLeftCheck and not bottomRightCheck else 0
    
    if checkTile(i, j, board, 1, letter):
        leftUpCheck = doesLineExist(i+1, j, 1, 1, board, visited, letter, True)
        leftDownCheck = doesLineExist(i-1, j, -1, 1, board, visited, letter, True)
        per += 1 if not leftUpCheck and not leftDownCheck else 0

    if checkTile(i, j, board, 3, letter):
        rightUpCheck =   doesLineExist(i+1, j, 1, 3, board, visited, letter, True)
        rightDownCheck = doesLineExist(i-1, j, -1, 3, board, visited, letter, True)
        
        per += 1 if not rightUpCheck and not rightDownCheck else 0
    
    if letter == "A":
        pass

    if i > 0:
        if not visited[i-1][j] and board[i-1][j] == letter:
            newArea, newPer = recur(i-1, j, board, visited, letter, (i, j))
            area, per = area + newArea, per + newPer
    if j > 0:
        if not visited[i][j-1] and board[i][j-1] == letter:
            newArea, newPer = recur(i, j-1, board, visited, letter, (i, j))
            area, per = area + newArea, per + newPer
    if i < len(board)-1:
        if not visited[i+1][j] and board[i+1][j] == letter:
            newArea, newPer = recur(i+1, j, board, visited, letter, (i, j))
            area, per = area + newArea, per + newPer
    if j < len(board[0])-1:
        if not visited[i][j+1] and board[i][j+1] == letter:
            newArea, newPer = recur(i, j+1, board, visited, letter, (i, j))
            area, per = area + newArea, per + newPer
    

    return area, per
        

        
    
        
def main():

    # Load the board
    board = []
    with open('map.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            ls = []
            for char in line:
                if char.isspace():
                    continue
                ls.append(char)
            board.append(ls)

    # Create the visited matrix
    visited = []
    for i in range(len(board)):
        new_row = []
        for j in range(len(board[0])):
            new_row.append(False)
        visited.append(new_row)
    
    # Traverse the board
    total_cost = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not visited[i][j]:
                area, perimeter = recur(i, j, board, visited, board[i][j], (None, None))
                total_cost += area*perimeter

    print(f"Total cost: {total_cost}")


        


if __name__ == "__main__":
    main()