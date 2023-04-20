# given a total number of steps and one step that cannot be stepped on, determine the farthest distance
# that can be reached given that step lengths can be equal to the interval that the step is taken in, or 
# it can be 0. for instance on interval 1, the step length can be 0 or 1. On step 2 the interval can be
# 0 or 2. On interval 3,  the step length can be 3 or 0 and so on.
def maxIndex(steps, badIndex):
    maxIndex = 0
    for step in range(steps+1):
        maxIndex +=step
    current_index = maxIndex
    step = steps

    while True:
        while current_index > 0 and step > 0:
            current_index -= step
            if (current_index == badIndex):
                current_index+=step
            step -=1
        if current_index<=0:
            return maxIndex
        else:
            step = steps
            current_index = maxIndex-1
            maxIndex-=1
            if current_index == badIndex:
                current_index = maxIndex-1
                maxIndex-=1
if __name__ == "__main__":
    print(maxIndex(40,10))