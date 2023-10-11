def min_coin_change(denoms: list[int], amt:int)->int:
    lower_sol = [float('inf')]*(amt+1)
    lower_sol[0] = 0
    for index in range(1,len(lower_sol)):
        for denom in denoms:
            if denom <= index:
                lower_sol[index] = min(lower_sol[index], lower_sol[index-denom] + 1)
    return lower_sol[-1] if lower_sol[-1] != float('inf') else -1

print(min_coin_change([1,2,5], 11))
