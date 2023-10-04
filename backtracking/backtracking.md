a list of backtracking problem solving:
creating many permutations from a list:
    define base case
    add an item to the list, perform an recursive call on that list
    pop the item


    1)amount: find all the permutations that add to an amount
        use a helper function to do the actual work and pass in a sorted list with mutable permutations and solutions lists
        set up a base case of if target = 0, append the permutation to a mutable solutions list and return
        if the list of numbers to choose from  = [] also return
        permutations:
            add and item to the permutation
            *perform a recursive call reducing the list of items by 1 from the beginning and reducing the target value by the item appended*
            pop the item and do so for each item in the list

    2) combo sum: return all the unique combos that add to a target
        This follows the same solution as amount, but before appending to the solution, it sorts the list to see if it already exists in the solution
        only add new solutions

    3) distinct permutations: still confused on this one
        1,2,3 = [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]

        the trick here is to set the returned value to an empty list at every call and build the list from scratch
        for each item in the list, take an item out of the list, recurse, take an item out, recurse.
        when a list of one item is called, return that item
        as you bubble up through the recursive calls, append the item taken out to each returned permutation

        in this way, 
        for the first loop
        on the way down: 123 => 23 =>3; 32 => 2
        up: 3=> 32=> 321 ; 2 => 23=> 231
        nums = 231
        ans = [[321], [231]]
        ons second loop
        down: 231 => 31=> 1 ; 231 => 13 => 3
        up: 1=>13=>132 ; 3 => 31=> 312
        nums = 312
        ans = [[321], [231]. [132],[312]]
        so on and so fourth

    4) nextPermutation:
        This is less a backtracking problem and more a lexigraphical list problem understanding which numbers to switch.
        starting from the left, you find the first decending set of of numbers, then switch the lowest number with the smallest number to it's right
    
    5) Palindrome substring: find all of the combinations of separated letters that makes a palindrome
    "aabaa" = [['a', 'a', 'b', 'a', 'a'], ['a', 'a', 'b', 'aa'], ['a', 'aba', 'a'], ['aa', 'b', 'a', 'a'], ['aa', 'b', 'aa'], ['aabaa']]

    break this problem into 3 pieces. 
    1)check for isPalindrome letters == letters[::-1]
    2)back track:
        base case, if the length of the current palindrom is that of the initial string append it to the result
        loop through each index value creating differnt sized lists from the start valuue to the inner loop value. in each loop call back track on what is left of the loop
        so the first call to backtrack should call is pal on string[0:1] and backtrack on [1:string length]
        use the append to answer can check if palidrome then pop methodology

        if we're not dealing with a palindrom, the list lengthens. if we are then we add to the result and check the rest of the list, setting a new start value to loop through the end.

        as we bubble back up the recursion, the letters at the end start to group, creating checking longer and longer sets for palindromes

        as we get groupings near the beginning, the letters at the end are re checked and added to the specific set that is appended to the answer group.
        you can imagine it like a wave that can get bigger and bigger as it bubbles back up the recursive tree

        append, check and then pop