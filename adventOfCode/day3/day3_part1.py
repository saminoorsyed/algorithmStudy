def sum_possible_numbers(lines):
    # use a two pointer system with the leading pointer adding to a dictionary
    # and the trailing pointer removing from the dictionary
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    top_line = 0
    sum_of_valid_nums = 0
    top = {}
    middle = {}
    bottom = {}

    def check(cols_to_check):
        for col in cols_to_check:
            # check the values around each value
            # check the three values above
            if top and col-1 >= 0 and top[col-1] not in digits and top[col-1] != ".":
                return True
            if top and top[col] not in digits and top[col] != ".":
                return True
            if top and col+1 <= 139 and top[col+1] not in digits and top[col+1] != ".":
                return True
            # check the three values below
            if bottom and col-1 >= 0 and bottom[col-1] not in digits and bottom[col-1] != ".":
                return True
            if bottom and bottom[col] not in digits and bottom[col] != ".":
                return True
            if bottom and col+1 <= 139 and bottom[col+1] not in digits and bottom[col+1] != ".":
                return True
            # check the adjacent values
            if col-1 >= 0 and middle[col-1] not in digits and middle[col-1] != ".":
                return True
            if col+1 <= 139 and middle[col+1] not in digits and middle[col+1] != ".":
                return True
        return False
    top_line = 0
    for bottom_line in range(len(lines)):
        # shift dictionaries down one
        top = middle
        middle = bottom
        bottom = {}
        for col in range(len(lines[bottom_line])):
            bottom[col] = lines[bottom_line][col]
        cols_to_check = []
        for col in middle.keys():
            if middle[col] in digits:
                cols_to_check.append(col)
            if cols_to_check and middle[col] not in digits:
                if check(cols_to_check):
                    number = ""
                    for digit in cols_to_check:
                        number += middle[digit]
                    sum_of_valid_nums += int(number)
                cols_to_check = []
    return sum_of_valid_nums


if __name__ == "__main__":
    file_path = '/home/sami/dev/osu_portfolio/algorithmStudy/adventOfCode/day3/input.txt'
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        final_line = ["." for x in lines[0]]
        lines.append(final_line)
    print(sum_possible_numbers(lines))
``