"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

e.g.
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

e.g.
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

e.g.
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

Solution
This problem follows the Two Pointers pattern and is quite similar to Triplet Sum to Zero.
We can follow a similar approach to iterate through the array, taking one number at a time. At every step, we will save the difference between the triplet and the target number, so that in the end, we can return the triplet with the closest sum.

Time Complexity
Sorting the array will take O(N* logN). Overall, the function will take O(N * logN + N^2), which is asymptotically equivalent to O(N^2)

Space Complexity
The above algorithm’s space complexity will be O(N), which is required for sorting.
------------------------------------------------------------------------

Consider edge cases, pay attention to the value of target sum. For the following cases, just draw out the horizontal bar x, we'll see easily why it's necessary.
# case 1: target sum > 0
    [-5, -2, 0, 2, 3, 5], -3
    (-5, -2, 5) => -1, min = -1 => the closest distance would be at this point
    (-5, -2, 3) =>  1, min = 1
# case 2: target sum < 0
    [-5, -2, 0, 2, 9, 11], 3
    (-5, -2, 11) => -1, min = -1
    (-5, -2, 9) =>  1, min = 1 => The closest distance would be at this point

The solution below I think is more applicable to case 1 because of (**).
"""


import math


def triplet_sum_close_to_target(array, target_sum):
    array.sort()
    min_diff = math.inf

    # Whether range(len(array)) or range(len(array) -2) doesn't really make a differece here
    # since we have a subscondition set while left < right
    for i in range(len(array)):
        left, right = i+1, len(array) - 1

        while left < right:
            target_diff = target_sum - (array[i] + array[left] + array[right])
            if target_diff == 0:
                return target_sum

            if abs(target_diff) < abs(min_diff) or \
                    (abs(target_diff) == abs(min_diff) and target_diff > min_diff):
                min_diff = target_diff  # save the closest and the biggest difference ** (potentially only for a positive target sum)

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1  # we need a triplet with a smaller sum

    return target_sum - min_diff


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()