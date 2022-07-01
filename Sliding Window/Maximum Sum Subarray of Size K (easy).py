'''
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

e.g.
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

e.g.
Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

Solution

A basic brute force solution will be to calculate the sum of all ‘k’ sized subarrays of the given array to find the subarray with the highest sum. We can start from every index of the given array and add the next ‘k’ elements to find the subarray’s sum.

The time complexity of the above algorithm will be O(N).
The algorithm runs in constant space O(1).
'''


def max_sum_subarray_of_size_k(k, arr):
    window_start, window_sum, max_sum = 0, 0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, no need to slide if we've not hit the required window size of 'k'
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1   # slide the window ahead

    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sum_subarray_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sum_subarray_of_size_k(2, [2, 3, 4, 1, 5])))

main()
