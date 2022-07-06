"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the triplets array.
How would the time and space complexity change from the previous similar problem that return only the count value?
e.g.
Input: [-1, 0, 2, 3], target=3
Output: [-1, 0, 3], [-1, 0, 2]
Explanation: There are two triplets whose sum is less than the target:

e.g.
Input: [-1, 4, 2, 1, 3], target=5
Output: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


Solution
This problem follows the Two Pointers pattern and shares similarities with Triplet Sum to Zero. The only difference is that, in this problem, we need to find the triplets whose sum is less than the given target. To meet the condition i != j != k we need to make sure that each number is not used more than once.
Following a similar approach, first, we can sort the array and then iterate through it, taking one number at a time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that X + Y + Z < targetX+Y+Z<target. At this stage, our problem translates into finding a pair whose sum is less than “target - Xtarget−X” (as from the above equation Y + Z == target - XY+Z==target−X). We can use a similar approach as discussed in Triplet Sum to Zero.

Time Complexity
Sorting the array will take O(N * logN)O(N∗logN). The searchPair(), in this case, will take O(N^2)
the main while loop will run in O(N)O(N) but the nested for loop can also take O(N)O(N) - this will happen when the target sum is bigger than every triplet in the array.
So, overall searchTriplets() will take O(N * logN + N^3) which is asymptotically equivalent to O(N^3)O(N


Space Complexity
Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.
"""


def triplet_with_smaller_sum(array, target):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        search_pairs(array, target - array[i], i, triplets)
    return triplets


def search_pairs(array, target, first, triplets):
    left, right = first + 1, len(array) - 1

    while left < right:
        if array[left] + array[right] < target:  # found the triplet
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any
            # number between left and right to get a sum less than the target sum
            for i in range(right, left, -1):
                triplets.append([array[first], array[left], array[right]])
            left += 1
        else:
            right -= 1  # we need a pair with a smaller sum
    return triplets


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 1, 2, 3, 4], 5))


main()
#   [[-1, 0, 3], [-1, 0, 3]]
#   [[-1, 1, 4], [-1, 1, 4], [-1, 1, 4], [-1, 2, 3]]



