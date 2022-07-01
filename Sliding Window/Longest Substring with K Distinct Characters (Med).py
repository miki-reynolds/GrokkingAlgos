'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

e.g.
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

e.g.
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

e.g.
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Solution

This problem follows the Sliding Window pattern, and we can use a similar dynamic sliding window strategy as discussed in Smallest Subarray with a Greater Sum. We can use a HashMap to remember the frequency of each character we have processed. Here is how we will solve this problem:

First, we will insert characters from the beginning of the string until we have K distinct characters in the HashMap.
These characters will constitute our sliding window. We are asked to find the longest such window having no more than K distinct characters. We will remember the length of this window as the longest window so far.
After this, we will keep adding one character in the sliding window (i.e., slide the window ahead) in a stepwise fashion.
In each step, we will try to shrink the window from the beginning if the count of distinct characters in the HashMap is larger than K. We will shrink the window until we have no more than K distinct characters in the HashMap. This is needed as we intend to find the longest window.
While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the HashMap if its frequency becomes zero.
At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember its length.

The above algorithm’s time complexity will be O(N)O(N), where NN is the number of characters in the input string. The outer for loop runs for all characters, and the inner while loop processes each character only once; therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N)O(N).
The algorithm’s space complexity is O(K)O(K), as we will be storing a maximum of K+1 characters in the HashMap.
'''


def longest_substring_with_k_distinct(string, k):
    window_start, max_length = 0, 0
    char_frequency = {}
    # shrink the sliding window, until we are left with 'k' distinct characters in
    # the char_frequency
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        #  it stops when len(char_frequency) == k -> we're left with exactly k distinct characters
        while len(char_frequency) > k:
            left_char = string[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1          # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print("Length of the longest substring: "
             + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: "
             + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: "
             + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
# 4, 2, 5