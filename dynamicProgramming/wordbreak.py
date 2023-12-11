"""Word Break Problem: Given a string and a dictionary of words, determine if the string can be segmented into a space-separated sequence of one or more dictionary words.

For example,

Input:
 
dict[] = { this, th, is, famous, Word, break, b, r, e, a, k, br, bre, brea, ak, problem };
 
word = Wordbreakproblem
 
Output:
 
Word b r e a k problem
Word b r e ak problem
Word br e a k problem
Word br e ak problem
Word bre a k problem
Word bre ak problem
Word brea k problem
Word break problem"""

# give all combinations of the answer
#  the naive way to do this is to iterate over the list figuring out all the permutations that make up the answer n^n
# lets do a DP this should take n^2 time

#  Here we can work backwards, building the original string in as many ways as posible and saving our results

def wordBreak(word: str, dictionary: list[str])-> list[str]:
    """ returns all the different permutations of the dictionary that combine to form the word"""
    # here we have to consider that the word can be broken down into characters, we'll store all the solutions for up to a character at that characters index 
    dp = [[] for char in word]

    char_string = ''
    for index, char in enumerate(word):
        # add the next character to the char string
        char_string+= word[index]
        # match the character string starting from the beginning to all possible combinations that might make it up
        for item in dictionary:
            item_length = len(item)
            char_string_len = len(char_string)
            if item_length > len(char_string):
                continue
            # if the item from the dictionary matches the characters at the end of the character string
            # check whether the solution for the rest of the word exists, if so, add that sol to the current
            checker = char_string[char_string_len:item_length:-1]
            if item == char_string[char_string_len-1:item_length-1:-1]:
                # add the solution if there the word is completed up to this point
                for string_sol in dp[index - item_length]:
                    dp[index].append(string_sol+' '+item)
    return dp[-1]


                    
                
dict = [ 'this', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r', 'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem'];
 
word = 'Wordbreakproblem'

print(wordBreak(word, dict))