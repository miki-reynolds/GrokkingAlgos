"""
Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

e.g.
Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

e.g.
Input: [8, 2, 6, 5], target=50
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
Explanation: There are seven contiguous subarrays whose product is less than the target.

Solution
This problem follows the Sliding Window and the Two Pointers pattern and shares similarities with Triplets with Smaller Sum with two differences:
In this problem, the input array is not sorted.
Instead of finding triplets with sum less than a target, we need to find all subarrays having a product less than the target.
The implementation will be quite similar to Triplets with Smaller Sum.


Time Complexity
The main for-loop managing the sliding window takes O(N) but creating subarrays can take up to O(N^2) in the worst case.
Therefore overall, our algorithm will take O(N^3)

Space Complexity
Ignoring the space required for the output list, the algorithm runs in O(N) space which is used for the temp list.
Can you try estimating how much space will be required for the output list?

The worst-case will happen when every subarray has a product less than the target!
So the question will be, how many contiguous subarrays an array can have?
It is definitely not all Permutations of the given array; is it all Combinations of the given array?
It is not all the Combinations of all elements of the array!

For an array with distinct elements, finding all of its contiguous subarrays is like finding the number of ways to choose two indices, i and j, in the array such that i <= j.

If there are a total of n elements in the array, here is how we can count all the contiguous subarrays:

When i = 0, j can have any value from 0 to n-1, giving a total of n choices.
When i = 1, j can have any value from 1 to n-1, giving a total of n-1 choices.
Similarly, when i = 2, j can have n-2 choices.
      …
      …
When i = n-1, j can only have only 1 choice.
Let’s combine all the choices:
    n + (n-1) + (n-2) + ... 3 + 2 + 1
Which gives us a total of: n*(n+1)/2
So, at most, we need space for O(n^2) output lists. At worst, each subarray can take O(n)O(n) space, so overall, our algorithm’s space complexity will be O(n^3)
"""


# read about deque at the bottom
from collections import deque


def find_subarrays(array, target):
    product = 1
    result = []
    left = 0
    # count = 0

    for right in range(len(array)):
        product *= array[right]

        while product >= target and left < len(array):
            # shed left number off because of the subcontiguousness;
            # this is also the reason we don't need sorted array like Nth-sum problem
            product /= array[left]
            left += 1  # incrementing left to the next position

        # since the product of all numbers from left to right is less than the target
        # therefore, all subarrays from left to right will have a product less than the
        # target too; to avoid duplicates, we will start with a subarray containing only
        # arr[right] and then extend it
        temp_subarray = deque()  # in this case, we use Deque for FILO though Deque can be utilized both ways.

        for i in range(right, left - 1, -1):  # (left - 1) so left can be included! Remember how range works!
            temp_subarray.appendleft(array[i])  # honestly, append shows the same result
            result.append(list(temp_subarray))
            # count += 1

    return result


# Count Numbers of Subarrays Whose Products < K
# BigO Time O(N) and Space O(1)
def count_subarrays_of_smaller_k_produc6(nums, k):
    if k <= 1:
        return 0
    start, count, product = 0, 0, 1
    for end in range(len(nums)):
        product *= nums[end]
        while product >= k:
            product /= nums[start]
            start += 1
        count += end - start + 1
    return count

"""
Approach #1: Binary Search on Logarithms [Accepted]
Intuition
Because log(II.i X.i) = sum.i(logX.i), we can reduce the problem to subarray sums instead of subarray products. The motivation for this is that the product of some arbitrary subarray may be way too large (potentially 1000^50000), and also dealing with sums gives us some more familiarity as it becomes similar to other problems we may have solved before.

Algorithm
After this transformation where every value x becomes log(x), let us take prefix sums 
prefix[i+1] = nums[0] + nums[1] + ... + nums[i]. Now we are left with the problem of finding, 
for each i, the largest j so that nums[i] + ... + nums[j] = prefix[j] - prefix[i] < k.

Because prefix is a monotone increasing array, this can be solved with binary search. 
We add the width of the interval [i, j] to our answer, which counts all subarrays [i, k] with k <= j.
"""
import bisect
import math


def numSubarrayProductLessThanK(self, nums, k):
    if k == 0: return 0
    k = math.log(k)

    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + math.log(x))

    ans = 0
    for i, x in enumerate(prefix):
        j = bisect.bisect(prefix, x + k - 1e-9, i + 1)
        ans += j - i - 1
    return ans


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))

main()
# [2], [5], [2, 5], [3], [5, 3], [10]
# [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]


"""
Deque is more time-efficient for left operations,
>>> from collections import deque

Append and pop operations on both ends of a deque object are stable and equally efficient because deques are implemented as a doubly linked list. Additionally, append and pop operations on deques are also thread safe and memory efficient. These features make deques particularly useful for creating custom stacks and queues in Python.
Deques are also the way to go if you need to keep a list of last-seen items because you can restrict the maximum length of your deques. If you do so, then once a deque is full, it automatically discards items from one end when you append new items on the opposite end.

Here’s a summary of the main characteristics of deque:
Stores items of any data type
Is a mutable data type
Supports membership operations with the in operator
Supports indexing, like in a_deque[i]
Doesn’t support slicing, like in a_deque[0:2]
Supports built-in functions that operate on sequences and iterables, such as len(), sorted(), reversed(), and more
Doesn’t support in-place sorting
Supports normal and reverse iteration
Supports pickling with pickle
Ensures fast, memory-efficient, and thread-safe pop and append operations on both ends

Option	Description
insert(i, value)	Insert an item value into a deque at index i.
remove(value)	    Remove the first occurrence of value, raising ValueError if the value doesn’t exist.
a_deque[i]	        Retrieve the item at index i from a deque.
del a_deque[i]	    Remove the item at index i from a deque.
"""