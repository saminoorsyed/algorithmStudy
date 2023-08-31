def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    if n == 2 :
        return "11"
    number_str = countAndSay(n-1)
    count = 1
    new_string = ""
    for index in range(len(number_str)):
        if index == len(number_str)-1 or number_str[index] != number_str[index+1]:
            new_string = new_string + str(count)
            new_string = new_string + number_str[index]
            count = 1
        else:
            count +=1
    return new_string

if __name__ == "__main__":
    n = 5
    print(countAndSay(5))