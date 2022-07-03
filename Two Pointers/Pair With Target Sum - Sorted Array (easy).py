'''
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

e.g.
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

e.g.
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

Time and Space Complexity: The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
The algorithm runs in constant space O(1).

If used Binary Search, time complexity is O(N * logN).
'''


def pair_with_target_sum(array, target_sum):
    left, right = 0, len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            return [left, right]
        elif current_sum < target_sum:
            left += 1
        elif current_sum > target_sum:
            right -= 1

    return [-1, -1]


def main():
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))


main()
# [1, 3]
# [0, 2]
