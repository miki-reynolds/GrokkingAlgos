"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23
Output: true (23 is a happy number)
Explanations: Here are the steps to find out that 23 is a happy number:

Example 2:
Input: 12
Output: false (12 is not a happy number)
Explanations: Here are the steps to find out that 12 is not a happy number:

Solution
The process, defined above, to find out if a number is a happy number or not, always ends in a cycle. If the number is a happy number, the process will be stuck in a cycle on number ‘1,’ and if the number is not a happy number then the process will be stuck in a cycle with a set of numbers. As we saw in Example-2 while determining if ‘12’ is a happy number or not, our process will get stuck in a cycle with the following numbers: 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
We saw in the LinkedList Cycle problem that we can use the Fast & Slow pointers method to find a cycle among a set of elements. As we have described above, each number will definitely have a cycle. Therefore, we will use the same fast & slow pointer strategy to find the cycle and once the cycle is found, we will see if the cycle is stuck on number ‘1’ to find out if the number is happy or not.

Time Complexity
The time complexity of the algorithm is difficult to determine. However we know the fact that all unhappy numbers eventually get stuck in the cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

This sequence behavior tells us two things:
If the number N is less than or equal to 1000, then we reach the cycle or ‘1’ in at most 1001 steps.
For N > 1000, suppose the number has ‘M’ digits and the next number is ‘N1’. From the above Wikipedia link, we know that the sum of the squares of the digits of ‘N’ is at most 9^2M, or 81M81M (this will happen when all digits of ‘N’ are ‘9’).
This means:

N1 <81M
As we know M = log(N+1)
Therefore: N1 < 81 * log(N+1)
=> N1 = O(logN)N1=O(logN)
This concludes that the above algorithm will have a time complexity of O(logN).

Space Complexity
The algorithm runs in constant space O(1).
"""


def happy_number(num):
    slow, fast = num, num

    while True:
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps

        if slow == fast:  # found the cycle
            break

    return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
    _sum = 0

    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10

    return _sum