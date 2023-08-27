def intToRoman(num: int) -> str:
    roman_numerals = [ "I", "VI", "V", "XI", "X", "LX", "L", "CX", "C", "DC", "D", "MC", "M"]
    mods = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    final = ""
    roman = 0
    #  from one through to the end
    for  mod in mods[::-1]:
        roman_numerals={
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        final = ''
        for value, sym in roman_numerals.items():
            count = num//value
            num -= value *count
            final += sym*count
        return final

    

if __name__ == "__main__":
    num = 58
    print(intToRoman(num))