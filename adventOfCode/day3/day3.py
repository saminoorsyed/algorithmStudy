def sum_possible_numbers(lines):
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    gears = {}
    summed_ratios = 0
    def find_adjacent_numbers(row, col):
        places_with_nums = {} # so that we don't double count numbers
        count = 0
        places_to_check = [(-1, -1), (-1, 0), (-1, 1),
                           (1, -1), (1, 0), (1, 1),
                           (0, -1), (0, 1)]
        for place in places_to_check:
            y,x = row+place[0], col+place[1]
            # dont check if it's out of range, or the place has already been checked
            if x>=0 and y>= 0 and x<= 139 and y<=139 and lines[y][x] in digits and (y,x) not in places_with_nums:
                count += 1
                # find the entire number that is adjacent to the star
                first, last = find_whole_number(y, x)
                ratio = ""
                for digit in range(first, last):
                    ratio += lines[y][digit]
                    places_with_nums[y,digit] = True
                if count == 1:
                    adjacent1 = int(ratio)
                elif count == 2:
                    adjacent2 = int(ratio)
        # if there's not exactly two adjacent numbers, dont count it
        if count !=2:
            return 0
        return adjacent1 * adjacent2
    
    def find_whole_number(row,col):
        left = right = col
        while left >= 0 and lines[row][left] in digits:
            left -=1
        while right <= 139 and lines[row][right] in digits:
            right +=1
        return (left+1, right)
        
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "*":
                summed_ratios += find_adjacent_numbers(row, col)

    return summed_ratios


if __name__ == "__main__":
    file_path = './input.txt'
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
    print(sum_possible_numbers(lines))
