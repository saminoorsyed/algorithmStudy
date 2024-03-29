#  figure out all the different ways to take n steps if you can take steps in increments of 1 or 2, the number of steps possible

# Approach: here we need to recognize that all steps are made up of combinations of the numbers 1 and 2. Recognizing this, we need can surmize that the current solution is sum of the sol[i-1] and sol[i-2].

#solutions list

def one_two_step(n: int)-> int:
    """ heres the idea is that we don't have to complete all the steps if there are over lapping ways to do it so here we build the solution from a small number of steps to a large number of steps, the current solution is the addition of the previous two steps"""
    step_sol = [0]*(n+1)
    step_sol[0] = 0
    step_sol[1] = 1
    step_sol[2] = 2
    step = 3
    while step <= n:
        step_sol[step] = step_sol[step-1]+step_sol[step-2]
        step+=1

    return step_sol[-1]

print(one_two_step(5))
