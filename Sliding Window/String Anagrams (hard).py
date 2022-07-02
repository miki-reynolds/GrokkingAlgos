'''
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

e.g.
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

e.g.
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
Solution

This problem follows the Sliding Window pattern and is very similar to Permutation in a String. In this problem, we need to find every occurrence of any permutation of the pattern in the string. We will use a list to store the starting indices of the anagrams of the pattern in the string.

Time Complexity


The time complexity of the above algorithm will be O(N + M)O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity

The space complexity of the algorithm is O(M)O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. In the worst case, we also need O(N)O(N) space for the result list, this will happen when the pattern has only one character and the string contains only that character.

'''


def find_string_anagrams(string, pattern):
    if len(pattern) > len(string):
        return []

    window_start, matched = 0, 0
    char_frequency = {}
    result_indices = []
    # get frequency of each character in the pattern
    for ch in pattern:
        if ch not in char_frequency:
            char_frequency[ch] = 0
        char_frequency[ch] += 1

    # Our goal is to match all the characters from the 'char_frequency' with the current
    # window try to extend the range [window_start, window_end]
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_frequency:
            # Decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(pattern): # Have we found an anagram?
            result_indices.append(window_start)
        # if the current substring's len >= pattern's len != matched, this current substring isn't the perm
        # so we gotta increment window_start to shrink the sliding window
        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            window_start += 1
            # if the left_char is the one sliding out of the window
            # we gotta decrement the matched and increment the left_char's frequencies again.
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1  # Before putting the character back, decrement the matched count
                char_frequency[left_char] += 1  # Put the character back

    return result_indices


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()