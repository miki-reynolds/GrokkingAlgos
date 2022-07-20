'''
Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="aabdec", Pattern="abac"
Output: "aabdec"
Explanation: The smallest substring having all characters occurrences of the pattern is "aabdec"
Example 3:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 4:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern

Solution

This problem follows the Sliding Window pattern and has a lot of similarities with Permutation in a String with one difference. In this problem, we need to find a substring having all characters of the pattern which means that the required substring can have some additional characters and doesn’t need to be a permutation of the pattern. Here is how we will manage these differences:

We will keep a running count of every matching instance of a character.
Whenever we have matched all the characters, we will try to shrink the window from the beginning, keeping track of the smallest substring that has all the matching characters.
We will stop the shrinking process as soon as we remove a matched character from the sliding window. One thing to note here is that we could have redundant matching characters, e.g., we might have two ‘a’ in the sliding window when we only need one ‘a’. In that case, when we encounter the first ‘a’, we will simply shrink the window without decrementing the matched count. We will decrement the matched count when the second ‘a’ goes out of the window.

Time Complexity
The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity
The space complexity of the algorithm is O(M since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. In the worst case, we also need O(N)O(N) space for the resulting substring, which will happen when the input string is a permutation of the pattern.

Self-explanation (Gist):
- At (**) point where we have a case of char_frequency[right_char] >= 0, why do we use >=
instead of == just like what we do in permutation problems, e.g. perms, anagrams?
Because we have to return a string data type, we gotta be accurate with the number of frequency
to ensure the accuracy of substring's indices and length.

- At (***), notice how we are comparing matched with len(pattern) vs
in the permutation cases where we don't care about returning a string,
we just compare matched (that is only incremented when char_frequency[right_char] == 0) with len(char_frequencies);
this will pit them against each other in terms of uniqueness of the characters.
Why? Once again, because we don't care about the positions.

- At (****), this is because only that one character is going out, and as soon as that happens,
the inner loop stops due to matched != len(pattern).
We then increment the left_char frequency back to the original dictionary.

'''


def find_smallest_substring_with_pattern(string, pattern):
    window_start, matched, substring_start = 0, 0, 0
    min_length = len(string) + 1
    char_frequency = {}

    for ch in pattern:
        if ch not in char_frequency:
            char_frequency[ch] = 0
        char_frequency[ch] += 1

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # Count every matching of a character **
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):  # ***
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substring_start = window_start  # set substring_start's value to window_start before we increment window_start

            left_char = string[window_start]
            window_start += 1
            if left_char in char_frequency:
                # Note that we could have redundant matching characters, therefore we'll
                # decrement the matched count only when a useful occurrence of a matched
                # character is going out of the window
                if char_frequency[left_char] == 0:  # why only decrementing when 0 and not for other occurrences? ****
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(string):
        return False
    return string[substring_start:substring_start+min_length]


def main():
    print(find_smallest_substring_with_pattern("aabdec", "abc"))
    print(find_smallest_substring_with_pattern("aabdec", "abac"))
    # print(find_smallest_substring_with_pattern("aabdec-c-dc", "abac"))
    print(find_smallest_substring_with_pattern("abdbca", "abc"))
    print(find_smallest_substring_with_pattern("adcad", "abc"))

main()