# Sami Noor Syed
# CS-325 Algorithms
# Assignment 7

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
    # use prims algorithm to construct an MST
    min_span_tree = Prims(G)
    print (min_span_tree)
    # construct a pre-order traversal walk through the MST
    # construct a hamiltonian circuit out of the pre-order traversal.
    # return a list in order from start to finish of the nodes visited along the walk


def Prims(G:list)->list:
    '''
input format: a graph is input as an adjacency matrix of the following form:
input = [ 
  [0, 8, 5, 0, 0, 0, 0], 
  [8, 0, 10, 2, 18, 0, 0], 
  [5, 10, 0, 3, 0, 16, 0], 
  [0, 2, 3, 0, 12, 30, 14], 
  [0, 18, 0, 12, 0, 0, 4], 
  [0, 0, 16, 30, 0, 0, 26], 
  [0, 0, 0, 14, 4, 26, 0] 
] 

The rows and columns of the matrix represent all the possible vertices.
Values to the left of the diagonal represent the 

Output: a list of tuples, wherein each tuple represents an edge of the MST as (v1, v2, 
weight) 
'''
    #store the number of vertices in the graph
    vertices = len(G)
    # create a list of tuples from the first row in G (distance, 0, new_node), exclude edges with a value of 0
    min_heap = [(G[0][j],0,j) for j in range(len(G)) if G[0][j] != 0]
    #create a heap structure from the list of tuples
    heapq.heapify(min_heap)
    # starting at node 0
    visited = [0]
    result = []
    # start a loop to go through all of the nodes until each has been visited
    while len(visited) < vertices:

        # pop the edje with the shortest distance in the heap off
        closest_node = heapq.heappop(min_heap)

        if closest_node[2] not in visited:
            visited.append(closest_node[2])
            result.append((closest_node[1], closest_node[2], G[closest_node[1]][closest_node[2]]))
            for i in range(len(G)):
                if G[closest_node[2]][i] != 0:
                    new_edge = (G[closest_node[2]][i], closest_node[2],i)
                    heapq.heappush(min_heap,new_edge)
    return result


if __name__ == "__main__":

    G = [ 
            [0, 2, 3, 20, 1], 
            [2, 0, 15, 2, 20], 
            [3, 15, 0, 20, 13], 
            [20, 2, 20, 0, 9], 
            [1, 20, 13, 9, 0], 
        ] 
    solve_tsp(G)