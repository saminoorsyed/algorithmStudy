List of Array problems grouped into similar problem solving techniques

# Single pass:
    1) replace with greatest to right:
        replace each element with the greatest value to it's right, replace the las el with -1\
        iterate from the end of the list to the beginning, keeping track of the max value so far encountered
        store the current element, replace it with the max value and then compare the stored value with the max value
        replace value it the stored value is larger
    2) zig zag: given a string, convert it to a ,matrix that represents a zig zag pattern of the letters
        first create a list of strings, one string for each row
        now you need two methods, one to place letters when zigging and one to place letters when zagging
        define your mod as the number of rows + rows -2. rows is for the zig and rows-2 is for the zag.
        if index % mod is less than rows, you are zigging, otherwise you are zagging. 
        for the zig, just place it in the string represented by index % mod
        for the zag, place the letter in the string represented by the mod value - (index % mod)
        concatenate all the lists and return
    



# PassThrough twice
    1) Array product except Self:
        Here, the goal is to build an answer array from left to right and then right to left multiplying the previous answer from the trailing and then leading index.
        array = [1,2,3,4]
        answer = [1,1,1,1]
        first pass: multiply by trailing index
        answer = [1,1,2,6]
        second pass: multiply by leading index
        answer = [24,12,8, 6]

    2) longest consecutive set:
        find the longest set of consecutive numbers 1, 2, 3, 4 in an unordered list
        first make a set of all the elements, then iterate through each element until the el +1 is not in the set
        increment count as long as el-1 is in the set. Once el -1 is not in the set, set longest to the max of the current val and new count
        this is O(n) time because at most you loop throught the list once. the look up for a set in python is O(1)

    3) sort colors:
        given colors red, white and blue represented by 0, 1, 2, sort an array of these integers so that each adjacent number is of the same type ie [0,0,0,1,1,1,2,2,2]
        
        count up the number of each integer in a single pass, then for each count, decrement the count as you place the color value at an index until the count is at 0. increment the index as you go

# Build a dictionary or set to check

    1) contains Duplicate:
        create a set using set() and check if the length is the same as the original list

        built ins:
        --set(): function called on a list, reduces to a set of unique values constant query time because python computes a hashcode for each item 

    2) grouping anagrams list[str]=> list[list[str]]:
        for each string in the original list, sort the string and use that sorted value as the key for the item in the dictionary
        if the key is not part of the dictionary, add an empty list to the dictionary under the key.
        append each item to the list associated with its key.

        built ins:
        --sorted(): a function that takes a list or string and returns a list in sorted order
        --"".join(sorted(item)): joins the list in the argument on an empty string to return a string of the sorted letters
        --dictionary.get(key, default_value): a built in method for dictionaries that returns a default value in absence of a key
        --dictionary.values: returns a list of all the values in a dictionary

    3) TwoSum:
        Given a list of ints, and a target value return the index of the two numbers that add to the target value
        Here we iterate through the list once, creating a dictionary of the form key: value = list value: list index
        upon iteration of each value in the list, we check if the difference of the value and the target is in the dictionary.
        if it is, we return that value from the dictionary and the current index in a list. if it is not, we add the current value to the dictionary with its index as the value.
    
    4) threeSum: find three numbers that add to 0 from a list
        first sort the items in the list then for each item in the list. then loop through each item. if an item > 0 there is no way for the numbers to sum to 0, so break and return an empty array. if the number is <= 0 then perform a two pointer with the number and a hi pointer as well as a low pointer if the sum is too low, increment the low number. if the sum is too high, decrement the high number if it's just right, append the indices, decrement hi and increment low. repeat until low = hi
    
    5) TopKFrequent: return the k most freq elements
        build a dictionary using the value at each index as a key and the count of each value as the value
        make a sorted list of the keys based on the values

        built-ins:
        --dictionary.keys(): returns a view object that should be cast to a list. the view object will change based on the dictionary in future calls. it points to the memory space of the dictionary. 
        --list():  casting to a list creates a copy of a list or a new list from an iterable including strings, tuples sets etc.
        --lambda functions: lambda arguments: expression
        --sorted(list(dict.keys()), key = lambda x: dict[x], reverse = true)
    
    6) is Anagram: check if two strings are anagrams
        first check if the lengths are equal (saves some time)
        build a dictionary of the characters and their count for the first string
        for each character in the second string, decrement the count in the dictionary
        if any count is <0, break and return false.

        built-ins:
        --dict.get(char to look for, default value to return if no char in dict)



# Building an answer using Modulo or floor division ore related arithmetic
    1) int to a roman numeral: 
        Create a dictionary of roman numerals key: string: including patters like 900: "CM" and 4: "IV"
        create a list of mods = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        loop through each mod from largest to smallest identifying how many of each and subtracting that value from the number until nothing is left

    2) is number palindrome without converting to a string:
        find the first digit with %10 and append it to a list, then number = number floor divide by 10.
        repeat until, appending each digit to a list until number = 0.
        compare the list to its reverse 

    3) my A to I:
        convert a number in string form to an integer
        Here we want to work through the number digit by digit, multiplying by 10^(reverse index) and adding to the final number
        "123" = 3*10^0+ 2*10^1 + 1*10^2
        on a question like this, edge cases like negatives and spaces or odd characters in the string are important to ask about



# Compare two lists:
    1) is Subsequence (do the letters of the first sequence, come in the same order of the second sequence):
        start a pointer at the beginning of each sequence. the pointer to the first seq is called searched and the pointer to the second is called searcher
        Increment the the searcher pointer until it points to the same val that searched points to, then increment both. if searched = len(seq1) return true, if searcher > len(seq2), return false letters in the searched list get found, then true, else false

    2) longest Common Prefix list[string]=> int:
        set the length and common word = to the first word in the list.
        loop through each word, comparing the letter in the new word to the common word (does not need to change) and incrementing a count
        after, if the count of letters is shorter than the length, set the length to the new count
    
    3) Merge in Place:
        given two lists , the first of length m + n and the second of length n, merge the lists together without creating a new list
        loop through the first list, incrementing i if the el from the first list is smaller and not 0
        else: insert the el from the second list and increment i and j (both pointers), don't forget to pop the last el from the first list
        Time complexity: this could possibly be O(n^2), one way to fix that is to swap the el in the first list with the el from the second list if the el from the second list is smaller. then there is no need to insert

        built ins:
        --array.insert(index, element): modifies the array in place and has a has a worst case time complexity of O(n)

# Priority Queue

    1) Sort que by height: given a queue of people, sort them by two values associated to each person, their height and the number of people of equal or greater height that can be in front of them
        first sort the queue by decending heightheight, then loop through the sorted queue and insert each person into an answer queue according to the number of people that can be in front of them

        built-ins:
        array.sort(key = lambda x: (-x[0], x[1])): .sort( key = None, reverse = False) modifies the existing list in place to ascending order. it has options to sort based on a key, or to reverse the order. in the above case, x represents the element of the list. and the tuple returned "(-x[0], x[1])" gives the priority of sorted order. first x[0], then x[1]
        the tuple can be extended 




