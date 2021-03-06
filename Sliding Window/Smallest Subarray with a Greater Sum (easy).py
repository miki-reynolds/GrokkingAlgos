'''
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

e.g.
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

e.g.
Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

e.g.
Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1]
or [1, 1, 6].

Solution

This problem follows the Sliding Window pattern, and we can use a similar strategy as discussed in Maximum Sum Subarray of Size K. There is one difference though: in this problem, the sliding window size is not fixed. Here is how we will solve this problem:

First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to ‘S.’
These elements will constitute our sliding window. We are asked to find the smallest such window having a sum greater than or equal to ‘S.’ We will remember the length of this window as the smallest window so far.
After this, we will keep adding one element in the sliding window (i.e., slide the window ahead) in a stepwise fashion.
In each step, we will also try to shrink the window from the beginning. We will shrink the window until the window’s sum is smaller than ‘S’ again. This is needed as we intend to find the smallest window. This shrinking will also happen in multiple steps; in each step, we will do two things:
Check if the current window length is the smallest so far, and if so, remember its length.
Subtract the first element of the window from the running sum to shrink the sliding window.

The time complexity of the above algorithm will be O(N). The outer for loop runs for all elements, and the inner while loop processes each element only once; therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N)O.
The algorithm runs in constant space O(1).


Self-explanation (Gist):
Please refer to "Smallest Window containing Substring" problem.
At the (**) point where we have a case of char_frequency[right_char] >= 0, why do we use >= instead of == just like what we do in permutation problems, e.g. perms, anagrams?
Because we have to return a string data type, we gotta be accurate with the number of frequency to ensure the accuracy of substring's indices and length. At (***), notice how we are comparing matched with len(pattern) vs in the permutation cases where we don't care about returning a string, we just compare matched (that is only incremented when char_frequency[right_char] == 0) with len(char_frequencies); this will pit them against each other in terms of uniqueness of the characters. Why? Once again, because we don't care about the positions.
'''


import math


def smallest_subarray_sum(s, arr):
    window_start, window_sum, min_length = 0, 0, math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == math.inf:
        return 0
    return min_length


def main():
    print("Smallest subarray length: "
       + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: "
       + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: "
       + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))


main()
