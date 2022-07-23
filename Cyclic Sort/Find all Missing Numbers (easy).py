"""
1. Cyclic Sort
    We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
    The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

    e.g.
    Input: [2, 3, 1, 8, 2, 3, 5, 1]
    Output: 4, 6, 7
    Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
    Example 2:

    Input: [2, 4, 1, 2]
    Output: 3
    Example 3:

    Input: [2, 3, 2, 1]
    Output: 4

    Solution
    This problem follows the Cyclic Sort pattern and shares similarities with Find the Missing Number with one difference.
    In this problem, there can be many duplicates whereas in ‘Find the Missing Number’
    there were no duplicates and the range was greater than the length of the array.

    However, we will follow a similar approach though as discussed in Find the Missing Number to place the numbers on their correct indices.
    Once we are done with the cyclic sort we will iterate the array to find all indices that are missing the correct numbers.

    Time Complexity
    The time complexity of the above algorithm is O(n).

    Space Complexity
    Ignoring the space required for the output array, the algorithm runs in constant space O(1).


*********************************************************************************************************
Two cases (Sorted Array With A One Increment For Each Element)
2. Single Missing Element in An Array
    a. Natural Nums (1,2,3,4,5,...)
    b. Non-natural Nums (9,10,11,12,13....)

    Missing_Ele = Sum of Natural Nums - Sum of Array
    Missing_Ele = Index_Difference + Difference (Index & Element)

3. Multiple Missing Elements in An Array
    a. Sorted Array
    b. Non-Sorted Array

"""

# Range from 1 -> N
def find_missing_numbers_cyclic_sort(nums):
    i, n = 0, len(nums)
    missing_elements = []

    while i < n:
        j = nums[i] - 1

        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1


    for i in range(n):
        if nums[i] != (i + 1):
            missing_elements.append(i + 1)

    return missing_elements


# [1, 2, 3, 4, 8, 9]
#  0  1  2  3  4  5
# Multiple Elements in Sorted Array
def find_multiple_missing_elements_in_sorted_nums(array):
    length = len(array)
    if not length:
        return "Empty Array"

    missing_eles = []
    diff_init = array[0] - 0
    for i in range(length):
        current_diff = array[i] - i

        if diff_init != current_diff:
            # condition to break the iteration to find missing elements
            while diff_init < current_diff:
                missing_ele = i + diff_init
                missing_eles.append(missing_ele)
                diff_init += 1

    return missing_eles


# Time O(n) - works for UNSORTED Array (Hashing)
# [9, 1, 3, 10, 8, 2
#  1  2  3  4   5  6
def find_multiple_missing_elements_in_unsorted_nums(array):
    length = len(array)
    if not length:
        return "Empty Array"

    whole_array = dict()
    missing_eles = []

    for i in range(length):
        whole_array[array[i]] = 1
    #  {
    #   '2': 1,
    #   '1': 2,
    #   '3': 3,
    #   '10': 4,
    #   '8': 5,
    #   '9': 6
    #   }

    low = min(array)    # low = 2
    high = max(array)  # high = 9
    while low <= high:
        if not whole_array.get(low):
            missing_eles.append(low)
        low += 1

    return missing_eles


def main():
    print(find_missing_numbers_cyclic_sort([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers_cyclic_sort([2, 4, 1, 2]))
    print(find_missing_numbers_cyclic_sort([2, 3, 2, 1]))
    # Abdul
    print(find_multiple_missing_elements_in_sorted_nums([1, 2, 3, 4, 8, 9]))
    print(find_multiple_missing_elements_in_unsorted_nums([2, 1, 3, 10, 8, 9]))


main()
