'''
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

e.g.
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

e.g.
Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

Solution
This is a straightforward question. The only trick is that we can have negative numbers in the input array, which will make it a bit difficult to generate the output array with squares in sorted order.
An easier approach could be to first find the index of the first non-negative number in the array. After that, we can use Two Pointers to iterate the array. One pointer will move forward to iterate the non-negative numbers, and the other pointer will move backward to iterate the negative numbers. At any step, whichever number gives us a bigger square will be added to the output array. For the above-mentioned Example-1, we will do something like this:

Time Complexity
The above algorithm’s time complexity will be O(N) as we are iterating the input array only once.

Space Complexity
The above algorithm’s space complexity will also be O(N); this space will be used for the output array.
'''


def make_squares(array):
    length = len(array)
    squares_array = [0 for i in range(length)]
    highest_square_index = length - 1
    left, right = 0, length - 1

    # why not '<' yet '<='? Because it is an index in the array we try to create,
    # two numbers created from the same index in the original array will be the same number.
    while left <= right:
        left_square = array[left] * array[left]
        right_square = array[right] * array[right]

        if left_square > right_square:
            squares_array[highest_square_index] = left_square
            left += 1
        else:  # left_square <= right_square
            squares_array[highest_square_index] = right_square
            right -= 1

        # either case in this SORTED array, we're going to have a highest square
        # decrement the highest square index.
        highest_square_index -= 1

    return squares_array


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
# Squares: [0, 1, 4, 4, 9]
# Squares: [0, 1, 1, 4, 9]
