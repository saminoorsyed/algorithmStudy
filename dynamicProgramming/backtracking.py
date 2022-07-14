def dna_match_bottomup(DNA1: list, DNA2: list) -> int:
    """
    bottom up solution to longest common subsequence problem
    """
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

def LCS_backtrack(list1: list, list2: list) -> list:
    """
    bottom up solution to longest common subsequence problem with backtracking
    """
    # cache = [[0 for x in range(n+1)] for x in range(m+1)]
    cache = [[0 for x in range(len(list1)+1)] for x in range(len(list2)+1)]
    for row in range(len(list2)+1):
        for column in range(len(list1)+1):
            if row == 0 or column == 0:
                cache[row][column] = 0
            elif list1[column-1] == list2[row-1]:
                cache[row][column] = cache[row-1][column-1]+1
            else:
                cache[row][column] = max(cache[row-1][column], cache[row][column-1])
    count = 0
    length1 = len(list1)
    length2 = len(list2)
    solution = []
    while count < cache[len(list2)][len(list1)]:
        if list1[length1-1] == list2[length2-1]:
            solution.append(list1[length1-1])
            length1 -= 1
            length2 -= 1
            count+=1
        elif cache[length2][length1] == cache[length2][length1-1]:
            length1 -=1
        else:
            
            length2 -= 1
    solution.reverse()
    return solution

if __name__ == '__main__':
    list1 = [1,6,3,4,5]
    list2 = [1,2,3,4]

    print(LCS_backtrack(list1,list2))