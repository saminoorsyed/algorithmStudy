# import the heapq module so that Prims can run using a min-heap
import heapq

def solve_tsp(G:list)->list:
    """
    given a traveling sales person problem, implement a heuristic algorithm to solve for the minimum distance hamiltonian circuit
    
    Input: The input Graph is provided in the form of a 2-D matrix (adjacency matrix). 
        Consider the first node as the starting point.  
        
        Sample input:  
        G = [ 
            [0, 2, 3, 20, 1], 
            [2, 0, 15, 2, 20], 
            [3, 15, 0, 20, 13], 
            [20, 2, 20, 0, 9], 
            [1, 20, 13, 9, 0], 
        ] 

    Output: A list of indices indicating the path taken. You must return the sequence of 
        nodes, the path taken starting from node 0. In this example, G is 5x5, indicating 
        there are 5 nodes in this graph: 0-4. You will always begin with node 0, and your 
        path should include every node exactly once, and only go between nodes with a 
        nonzero edge between them. Your path will end at the starting node.  
        Sample output (For above graph G): 
        [0, 4, 3, 1, 2, 0]   
        Note: Not all graphs are fully connected: some rows in G may have more than one 0. 
        These indicate absence of an edge.  
        Name your function solve_tsp(G). Name your file TSP.py. 
    """
    # Initialize all vertices as unvisited.
    unvisited = [i for i in range(1,len(G))]
    loop_stop = len(unvisited)
    # Select an arbitrary vertex, set it as the current vertex u. Mark u as visited.
    steps = [0]
    #start a loop that terminates only when it returns to the beginning
    while len(steps) <= loop_stop:
        # Set an arbitrarily large minimum
        min = 999999999
        # add a placeholder value
        steps.append(0)
        #since we're only checking these connections once, a heap will not improve time complexity
        for vertex in range(len(G)):
            weight = G[steps[-2]][vertex]
            # check that the vertex has not been visited, that there is an edge and that the edge's weight is less than any other edge 
            if weight > 0 and weight < min and vertex in unvisited:
                min = weight
                steps[-1] = vertex
        check = steps[-1]
        if steps[-1] == 0:
            return False
        unvisited.remove(steps[-1])
    steps.append(0)
    if 0 in steps[1:-1]:
        return False
    return steps


    # Find out the shortest edge connecting the current vertex u and an unvisited vertex v.

    # Set v as the current vertex u. Mark v as visited.

    # If all the vertices in the domain are visited, then terminate. Else, go to step 3.


if __name__ == "__main__":

    G = [ 
            [0, 2, 3, 20, 1], 
            [2, 0, 15, 2, 20], 
            [3, 15, 0, 20, 13], 
            [20, 2, 20, 0, 9], 
            [1, 20, 13, 9, 0], 
        ] 
    print(solve_tsp(G))