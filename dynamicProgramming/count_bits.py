"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105"""

def count_bits(n:int)->list[int]:
    answer = [0]*(n+1)
    if n == 0:
        return [0]
    answer[1] = 1
    for index in range(n+1):
        answer[index] = answer[index//2]+ index % 2
    return answer

if __name__ == "__main__":
    n = 5
    print(count_bits(n))
# Output: [0,1,1,2,1,2]