# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    final = [0]*len(temperatures)
    for index,temp in enumerate(temperatures):
        if stack:
            finalIndex = index-1
            count = 1
            # counting back if the temp is greater, this could result in n^2 time if the list is of ever increasing numbers
            while finalIndex>=0 and temp > stack[finalIndex]:
                if final[finalIndex] == 0:
                    final[finalIndex] = count
                count +=1
                finalIndex-=1
        stack.append(temp)
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
