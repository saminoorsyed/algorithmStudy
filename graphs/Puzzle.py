import copy
# copy allows a deep copy of the puzzle so that a separate variable can be a assigned to an equivalent board

def solve_puzzle(Board: list, Source: tuple, Destination: tuple)->list:
    """
    solves a 2-D puzzle of size MxN, that has N rows and M column (M and N can be different). Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’. Given are two coordinates from the puzzle (a,b) and (x,y). The start location is at (a,b) and the destination is (x,y).
    
    return: a list of tuples that represents the indices of each position in the shortest path from the start to the end location 
    """
    puzzle = copy.deepcopy(Board)
    # get dimensions of the board
    rows = len(puzzle)
    columns = len(puzzle[0])
    # initiate a list to store visited vertices as tuples starting with the source (row, column)
    visited = [(Source[0],Source[1])]
    # change the value of the space on the board containing the source to the tuple (row, column, distance from source)
    puzzle[Source[0]][Source[1]] = (Source[0],Source[1],0)
    # start a loop that does not end until no new vertices can be reached
    already_visited = 0
    while len(visited) != already_visited:
        # store the number of previously visited spaces
        already_visited = len(visited)
        # from the current nodes, check all possible unvisited nodes that are adjacent
        for space in visited:
            # iterate through each of the surrounding spaces
            # store the x and y coordinates of the current vertex
            y = space[0]
            x = space[1]
            # current vertex's distance from the source
            dist = puzzle[y][x][2]
            for step in [-1,1]:
                # check the y direction as long as the space is on the board
                if rows > y+step and y+step >= 0:
                    # if the space is empty, update the space with a tuple containing the current vertex and its distance + 1
                    if puzzle[y + step][x] == '-':
                        puzzle[y + step][x] = (y,x, dist+1)
                        # add that node to a list of visited nodes
                        visited.append((y + step, x))
                    # if the space is not a barrier update its value if a shorter path is found
                    elif puzzle[y + step][x] != '#':
                        if puzzle[y + step][x][2] > dist +1:
                            puzzle[y + step][x] = (y,x, dist+1)
                #check the x direction as long as the adjacent square is on the board
                if columns > x + step and x +step >=0:
                    if puzzle[y][x+ step] == '-':
                        puzzle[y][x+ step] = (y,x, dist+1)
                        # add that node to a list of visited nodes
                        visited.append((y, x + step))
                    # if the space is not a barrier update its value if a shorter path is found
                    elif puzzle[y][x+ step] != '#':
                        if puzzle[y][x+ step][2] > dist +1:
                            puzzle[y][x+ step] = (y,x, dist+1)
    
    
    #once the algorithm has gone through the whole board, check the tuple stored at the destination and trace it's path back through to the source
    result = [Destination]
    length = 2
    while Destination != Source:
        y = Destination[0]
        x = Destination[1]
        # if the destination was never reached by the algorithm, return None
        if puzzle[y][x] == '-':
            return None
        result.append((puzzle[y][x][0],puzzle[y][x][1]))
        Destination = (puzzle[y][x][0],puzzle[y][x][1])
    result.reverse()
    directions = ''
    for index in range(len(result)-1):
        # step down
        if result[index][0]+1 == result[index+1][0]:
            directions += 'D'
        if result[index][0]-1 == result[index+1][0]:
            directions += 'U'
        if result[index][1]+1 == result[index+1][1]:
            directions += 'R'
        if result[index][1]-1 == result[index+1][1]:
            directions += 'L'
    return (result, directions)

if __name__ == '__main__':
    board = [['-', '-', '-', '-', '-'],
            ['-', '-', '#', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['#', '-', '#', '#', '-'],
            ['-', '#', '-', '-', '-']]
    source = (0, 0)
    destination = (4, 4)

    solution  = solve_puzzle(board, source, destination)
    count = 0
    for space in solution[0]:
        if board[space[0]][space[1]] == '#':
            print(space)
    print (solution)