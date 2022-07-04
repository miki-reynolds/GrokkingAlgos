'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

e.g.
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

e.g.
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

Solution
This problem follows the Two Pointers pattern and shares similarities with Pair with Target Sum. A couple of differences are that the input array is not sorted and instead of a pair we need to find triplets with a target sum of zero.
To follow a similar approach, first, we will sort the array and then iterate through it taking one number at a time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that X + Y + Z == 0X+Y+Z==0. At this stage, our problem translates into finding a pair whose sum is equal to “-X−X” (as from the above equation Y + Z == -XY+Z==−X).

Another difference from Pair with Target Sum is that we need to find all the unique triplets. To handle this, we have to skip any duplicate number. Since we will be sorting the array, so all the duplicate numbers will be next to each other and are easier to skip.

Time Complexity
Sorting the array will take O(N * logN). The searchPair() function will take O(N). As we are calling searchPair() for every number in the input array, this means that overall searchTriplets() will take O(N * logN + N^2), which is asymptotically equivalent to O(N^2).

Space Complexity
Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.
'''


def search_triplets(array):
    # this is a manual way to do the sort method, same time O(nlogn) as the builtin method
    # for i in range(len(array)//2 + 1):
    #     if array[i] > array[i+1]:
    #         array[i], array[i+1] = array[i+1], array[i]
    array.sort()
    triplets = []

    # as the array is sorted, this problem becomes TwoSum problem, Y + Z = - X
    for i in range(len(array)):
        # skip same element to avoid duplicate triplets
        if i > 0 and array[i] == array[i-1]:
            continue
        # why left is i+1 and not i? i is X, so index of Y should be starting from 1
        # are we afraid (i+1) out of range?
        # No, even though we set max of i < len(array), we also set the condition that i+1 (left) < length-1 (right)
        two_sum(array, -array[i], i + 1, triplets)

    return triplets


def two_sum(array, target_sum, left, triplets):
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, left, right])
            left += 1
            right -= 1

            while left < right and array[left] == array[left-1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and array[right] == array[right+1]:
                right -= 1  # skip same element to avoid duplicate triplets

        elif current_sum < target_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()