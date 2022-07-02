'''
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

e.g.
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

e.g.
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
Solution

This problem follows the Sliding Window pattern and is quite similar to Longest Substring with same Letters after Replacement. The only difference is that, in the problem, we only have two characters (1s and 0s) in the input arrays.

Following a similar approach, we’ll iterate through the array to add one number at a time in the window. We’ll also keep track of the maximum number of repeating 1s in the current window (let’s call it maxOnesCount). So at any time, we know that we can have a window with 1s repeating maxOnesCount time, so we should try to replace the remaining 0s. If we have more than ‘k’ remaining 0s, we should shrink the window as we are not allowed to replace more than ‘k’ 0s.
Time Complexity
The above algorithm’s time complexity will be O(N), where ‘N’ is the count of numbers in the input array.

Space Complexity
The algorithm runs in constant space O(1).
'''


def length_of_longest_subarray(array, k):
    if k >= len(array):
        return 0

    window_start, max_length, max_ones_count = 0, 0, 0
    # Try to extend the range [window_start, window_end]
    for window_end in range(len(array)):
        if array[window_end] == 1:
            max_ones_count += 1
        # Current window size is from window_start to window_end, overall we have a maximum
        # of 1s repeating 'max_ones_count' times, this means we can have a window with
        # 'max_ones_count' 1s and the remaining are 0s which should replace with 1s.
        # Now, if the remaining 0s are more than 'k', it is the time to shrink the window as
        # we are not allowed to replace more than 'k' 0s
        if (window_end - window_start + 1 - max_ones_count) > k:
            if array[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print(length_of_longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()