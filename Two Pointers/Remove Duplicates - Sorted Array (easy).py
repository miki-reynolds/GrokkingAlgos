'''
Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once. The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of O(1).
Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

e.g.
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

e.g.
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

Solution
In this problem, we need to separate the duplicates in-place such that the resultant length of the array remains sorted. As the input array is sorted, therefore, one way to do this is to shift the elements left whenever we encounter duplicates. In other words, we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number. So our algorithm will be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we’ve seen.

Time and Space Complexity: The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
The algorithm runs in constant space O(1).
'''


def remove_duplicates(array):
    left = 0
    unique = 1  # there will always be one distinct element in the array

    for right in range(1, len(array)):
        if array[left] != array[right]:
            left += 1
            unique += 1
        if array[left] == array[right]:
            same = array.pop(left)
            array.append(same)

    return unique


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
