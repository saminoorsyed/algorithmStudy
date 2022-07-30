
import heapq
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
    # create a list of tuples from the first row in G that represents the distances from node 0 to each other node
    min_heap = [[(G[i][j], i, j,) for j in range(len(G[i]))] for i in range (len(G))]
    #create a heap structure from the list of tuples
    heapq.heapify(min_heap)
    result = []
    #start a loop to go through all of the nodes until each has been visited
    visited = [0]
    while len(visited) < vertices:
        #set an arbitrarily high number to begin the comparison at the start of each loop
        minimum = 999999
        # loop through each visited node and check its edges for the least value
        # to speed this up, we would create a min heap of all the values in this row and then append the deque from first item
        closest_node = heapq.heappop(min_heap)
        # 0 is the column value which represents the node traveled to
        if closest_node[0] not in visited:
            visited.append(closest_node[2])
            result.append(closest_node)
            for i in range(len(G)):
                newedge = G[closest_node[2]][i]
                heapq.heappush(min_heap,(newedge,closest_node[2], i))
    return result

if __name__ == '__main__':
    G = [[0, 9, 75, 0, 0],
         [9, 0, 95, 19, 42],
         [75, 95, 0, 51, 66],
         [0, 19, 51, 0, 31],
         [0, 42, 66, 31, 0]]

    print(Prims(G))
