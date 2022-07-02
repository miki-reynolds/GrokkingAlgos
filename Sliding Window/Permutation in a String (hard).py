'''
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
Solution

This problem follows the Sliding Window pattern, and we can use a similar sliding window strategy as discussed in Longest Substring with K Distinct Characters. We can use a HashMap to remember the frequencies of all characters in the given pattern. Our goal will be to match all the characters from this HashMap with a sliding window in the given string. Here are the steps of our algorithm:

Create a HashMap to calculate the frequencies of all characters in the pattern.
Iterate through the string, adding one character at a time in the sliding window.
If the character being added matches a character in the HashMap, decrement its frequency in the map. If the character frequency becomes zero, we got a complete match.
If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (i.e., total characters in the HashMap), we have gotten our required permutation.
If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern’s size. At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap.

Time Complexity
The above algorithm’s time complexity will be O(N + M), where ‘N’ and ‘M’ are the number of characters in the input string and the pattern, respectively.

Space Complexity
The algorithm’s space complexity is O(M) since, in the worst case, the whole pattern can have distinct characters that will go into the HashMap.

Self-Explanation (Gist):
When we deal with patterns, e.g. permutation, anagrams, we gotta have a matched variable to increment whenever we encounter all frequencies of each charater in the pattern.
Then compare matched with the char_frequency dictionary (HashMap).

--
Please refer to "Smallest Window containing Substring" problem.
At the (**) point where we have a case of char_frequency[right_char] >= 0, why do we use >= instead of == just like what we do in permutation problems, e.g. perms, anagrams?
Because we have to return a string data type, we gotta be accurate with the number of frequency to ensure the accuracy of substring's indices and length. At (***), notice how we are comparing matched with len(pattern) vs in the permutation cases where we don't care about returning a string, we just compare matched (that is only incremented when char_frequency[right_char] == 0) with len(char_frequencies); this will pit them against each other in terms of uniqueness of the characters. Why? Once again, because we don't care about the positions.

'''


def find_permutation(string, pattern):
    if len(pattern) > len(string):
        return "None"

    window_start, matched = 0, 0
    char_frequency = {}
    for ch in pattern:
        if ch not in char_frequency:
            char_frequency[ch] = 0
        char_frequency[ch] += 1
    # our goal is to match all the characters from the 'char_frequency' with the current
    # window try to extend the range [window_start, window_end]
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True
        # if the current substring's len >= pattern's len != matched, this current substring isn't the perm
        # so we gotta increment window_start to shrink the sliding window
        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            window_start += 1
            # if the left_char is the one sliding out of the window
            # we gotta decrement the matched and increment the left_char's frequencies again.
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()