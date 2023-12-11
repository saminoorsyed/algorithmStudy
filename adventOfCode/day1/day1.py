def calibration_numbers(s:str)->int:
    """ use a two pointer solution to find the right and left numbers"""
    digit_dict ={
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    digits = ("1","2","3","4","5","6","7","8","9")
    left = 0
    right = len(s)-1
    left_length = strings_to_nums(left, s)
    right_length = 0
    while s[left] not in digits and left_length == 0:
        left +=1
        left_length=strings_to_nums(left, s)
    while s[right]not in digits and right_length == 0:
        right-=1
        right_length = strings_to_nums(right, s)

    if right_length>0:
        s = s[:right]+ digit_dict[s[right:right + right_length]] + s[right+right_length:]
    if left_length>0 and right!=left:
        s = s[:left]+digit_dict[s[left:left + left_length]]+ s[left+left_length:]
    
    if left_length>0 and right !=left:
        combined = s[left]+s[right-left_length+1]
    else:
        combined = s[left]+s[right]

    return int(combined)

def strings_to_nums(index: int, cal_string:str)->int:
    """returns the length of the number string, 0 if not present"""
    digit_dict ={
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    # check each of the possible lengths
    for number_length in range(3,6):
        if len(cal_string) - index >= number_length and cal_string[index:number_length+index] in digit_dict:
                return number_length
    return 0



def sum_cal_numbers(cals:list[str])->int:
    final = 0
    for cal_string in cals:
        final += calibration_numbers(cal_string)
    return final

if __name__ == "__main__":
    # input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    # # should print 142
    # print(sum_cal_numbers(input))
    # Open the file in read mode ('r')
    file_path = '/home/sami/dev/osu_portfolio/algorithmStudy/adventOfCode/day1/calibration.txt'
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].strip()
    print(sum_cal_numbers(lines))
    # # Alternatively, you can iterate over the file object directly
    # with open(file_path, 'r') as file:
    #     for line in file:
    #         print(line.strip())


