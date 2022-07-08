# Sami Noor Syed
# Analysis of Algorithms
# Summer 2022
# Assignment: 3
# Due Date: July 11, 2022
# Description: Implementation of top-down, bottom up and Naive approaches to the DNA matching problem

def dna_match_topdown(DNA1: list, DNA2: list, memo: list = []) -> int:
    
    columns = len(DNA1)
    rows = len(DNA2)
    if not memo:
        memo = [ [-1]*columns for i in range(rows)]
    
    if columns == 0 or rows == 0:
        return 0

    if memo[rows-1][columns-1] != -1:
        return memo[rows-1][columns-1]
    elif DNA1[-1] == DNA2[-1]:
        memo[rows-1][columns-1] = 1 + dna_match_topdown(DNA1[:-1], DNA2[:-1], memo)
        return memo[rows-1][columns-1]
    else:
         memo[rows-1][columns-1] = max(dna_match_topdown(DNA1, DNA2[:-1], memo), dna_match_topdown(DNA1[:-1], DNA2, memo))
         return memo[rows-1][columns-1]


def dna_match_bottomup(DNA1: list, DNA2: list) -> int:

    # cache = [[0 for x in range(n+1)] for x in range(m+1)]
    cache = [[0 for x in range(len(DNA1)+1)] for x in range(len(DNA2)+1)]
    for row in range(len(DNA2)+1):
        for column in range(len(DNA1)+1):
            if row == 0 or column == 0:
                cache[row][column] = 0
            elif DNA1[column-1] == DNA2[row-1]:
                cache[row][column] = cache[row-1][column-1]+1
            else:
                cache[row][column] = max(cache[row-1][column], cache[row][column-1])
    return cache[len(DNA2)][len(DNA1)]


# if __name__ == '__main__':
#     list1 = [1,6,3,4,5]
#     list2 = [1,2,3,4]
#     print(dna_match_topdown(list1, list2))
#     print(dna_match_bottomup(list1,list2))
