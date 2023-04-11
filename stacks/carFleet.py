# There are n cars going to the same destination along a one-lane road. The destination is target miles away.

# You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

# Return the number of car fleets that will arrive at the destination.

# Approach:
# here it might be best to figure out all the times that a car would arrive in if they could pass
# if a cars position and time of arrival are both less, we know that car will form a fleet.
# therefore, we can subtract the number of cars that have those two traits, but make sure we only subtract them once
def carFleet(target: int, positions: list[int], speeds: list[int]) -> int:
    # we start with the number of fleets equal to the number of cars
    fleets = len(positions)
    # create a key of positions and arrival times so that we can look up times with ease
    key = {}
    for index, position in enumerate(positions):
        key[position]= (target-positions[index])/speeds[index]
    # initiate a stack 
    slowest = []
    # positions have to be sorted so that we can iterate in descending order
    positions.sort(reverse=True)
    # for each car, if the position and time values are less than the most recent slowest car, reduce the fleet by one
    for index, position in enumerate(positions):
        if slowest and key[position]<= slowest[-1]:
            fleets-=1
        # only add times that are greater (slower) than previous times
        if not slowest or key[position]>slowest[-1]:
            slowest.append(key[position])
    return fleets




if __name__ == "__main__":
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(carFleet(target, position, speed))
# Output: 3
# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
# The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
# Note that no other cars meet these fleets before the destination, so the answer is 3.
    target = 10
    position = [3]
    speed = [3]
    print(carFleet(target, position, speed))
# Output: 1
# Explanation: There is only one car, hence there is only one fleet.

    target = 12
    position = [4,0,5,3,1,2]
    speed = [6,10,9,6,7,2]
    print(carFleet(target,position,speed))
# Output: 1
# Explanation:
# The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
# Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.