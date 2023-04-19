# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemperatures( temperatures: list[int]) -> list[int]:
    stack = []
    final = [0]*len(temperatures)
    for index,temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            last = stack.pop()
            final[last] = index-last
        stack.append(index)
    return final


if __name__ == "__main__":

    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temperatures))
# Output: [1,1,4,2,1,1,0,0]

# Example 2:

    temperatures = [30,40,50,60]
    print(dailyTemperatures(temperatures))
# Output: [1,1,1,0]
# 
# Example 3:

    temperatures = [30,60,90]
    print(dailyTemperatures(temperatures))
# Output: [1,1,0]
