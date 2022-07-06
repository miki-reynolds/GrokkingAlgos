"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

e.g.S
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

e.g.
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
Solution

The brute force solution will be to use an in-place sorting algorithm like Heapsort which will take O(N*logN). Can we do better than this? Is it possible to sort the array in one iteration?
We can use a Two Pointers approach (because there are only 3 unique elements) while iterating through the array. Let’s say the two pointers are called low and high which are pointing to the first and the last element of the array respectively.
So while iterating, we will move all 0s before low and all 2s after high so that in the end, all 1s will be between low and high.

Time Complexity
The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.

Space Complexity
The algorithm runs in constant space O(1).
"""


def dutch_flag_sort(array):
    # all elements < low are 0, and all elements > high are 2
    # all elements from >= low < i are 1
    low, high = 0, len(array)
    i = 0

    while i <= high:
        if array[i] == 0:
            array[i], array[low] = array[low], array[i]
            # increment 'i' and 'low'
            i += 1
            low += 1

        elif array[i] == 2:
            array[i], array[high] = array[high], array[i]
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            high -= 1

        else:  # the case for arr[i] == 1, the middle ones, i.e. 1s, end up in the middle between 0s and 2s
            i += 1


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()


