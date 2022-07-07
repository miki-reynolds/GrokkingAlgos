"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

e.g.
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

e.g.
Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.

Solution
This problem follows the Two Pointers pattern and shares similarities with Triplet Sum to Zero.
We can follow a similar approach to iterate through the array, taking one number at a time. At every step during the iteration, we will search for the quadruplets similar to Triplet Sum to Zero whose sum is equal to the given target.

Time Complexity
Sorting the array will take O(N*logN)O. Overall searchQuadruplets() will take O(N * logN + N^3) which is asymptotically equivalent to O(N^3)O(N

Space Complexity
The space complexity of the above algorithm will be O(N) which is required for sorting.
"""


def four_sum(array, target):
    array.sort()
    quadruplets = []

    for i in range(len(array) - 3):
        # reverse-compare at each stage/loop to avoid duplicates.
        # it may seem like we're repeating the same thing, but we reverse-compare, so steps are actually not redundant.
        if i > 0 and array[i] == array[i-1]:
            continue
        for j in range(i+1, len(array) - 2):
            if j > i+1 and array[j] == array[j-1]:
                continue
            search_pairs(array, target, i, j, quadruplets)
    return quadruplets


def search_pairs(array, target, first, second, quadruplets):
    left, right = second + 1, len(array) - 1

    while left < right:
        current_sum = array[first] + array[second] + array[left] + array[right]
        if current_sum == target:
            quadruplets.append([array[first], array[second], array[left], array[right]])
            left += 1
            right -= 1
            while left < right and array[left] == array[left - 1]:
                left += 1  # skip same element to avoid duplicate quadruplets
            while left < right and array[right] == array[right + 1]:
                right -= 1  # skip same element to avoid duplicate quadruplets

        if current_sum > target:
            right -= 1
        else:
            left += 1
    return quadruplets


def main():
    print(four_sum([4, 1, 2, -1, 1, -3], 1))  # [-3, -1, 1, 4], [-3, 1, 1, 2]
    print(four_sum([2, 0, -1, 1, -2, 2], 2))  # [-2, 0, 2, 2], [-1, 0, 1, 2]


main()

