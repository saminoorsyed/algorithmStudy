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
0 -->    0
1 -->    1
2 -->   10
3 -->   11
4 -->  100
5 -->  101
6 -->  110
7 -->  111
8 --> 1000
9 --> 1001
10--> 1010
11--> 1011
12--> 1100
13--> 1101
14--> 1110
15--> 1111
16-->10000



20 --> 10100
 

Constraints:

0 <= n <= 105"""


# the trick here is figuring out the relationship from one set of bits to the next:
# so what is it?
# we have to look for patterns in the result
# looking at the above, we se an alternating pattern in the lease most significant bit
# the second least most significant bit alternates every two integers
# the third least most significant bit alternates every 3 integers.
# this is just how normal binary systems work 
# what we can do is structure our answer to be a bottom up solution:
# sol = sols[index //2]+ index%2
# since the answer is built off of previous answers, we only have to add the modulo 2 result. ie. 27// 2 = 13
# so the solution fo 27 is the same as the solution for 13 + 27 % 2


def count_bits(n:int)->list[int]:
    answer = [0]*(n+1)
    if n == 0:
        return [0]
    answer[1] = 1
    for index in range(n+1):
        answer[index] = answer[index//2]+ index % 2
    return answer

if __name__ == "__main__":
    n = 13
    print(count_bits(n))
# Output: [0,1,1,2,1,2]
