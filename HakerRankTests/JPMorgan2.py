def maxIndex(steps, badIndex):
    maxIndex = 0
    for step in range(steps+1):
        maxIndex +=step
    current_index = maxIndex
    step = steps

    while True:
        while current_index>0 and step > 0:
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