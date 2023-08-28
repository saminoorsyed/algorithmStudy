# given a total number of steps and one step that cannot be stepped on, determine the farthest distance
# that can be reached given that step lengths can be equal to the interval that the step is taken in, or 
# it can be 0. for instance on interval 1, the step length can be 0 or 1. On step 2 the interval can be
# 0 or 2. On interval 3,  the step length can be 3 or 0 and so on.
def max_step(tot_steps: int, no_step:int)-> int:
    #find the farthest distance without taking into account no_step
    max_steps = 0
    for step in range(tot_steps+1):
        max_steps += step
    #count backward, avoiding the no step until you get to step 0
    cur_step = 1
    while max_steps != 0:
        cur_step = max_steps
        for step in range(tot_steps):
            if cur_step - (tot_steps-step) == no_step:
                step+=1
            cur_step -= tot_steps - step
            if cur_step <= 0:
                return max_steps
        max_steps-=1
if __name__ == "__main__":
    #should be 819
    print(max_step(40,10))