"""
For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

e.g.
Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: All the employees are free between [3,5].

e.g.
Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employees are free between [4,6] and [8,9].

e.g.
Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employees are free between [5,7].

Solution
This problem follows the Merge Intervals pattern. Let’s take the above-mentioned example (2) and visually draw it:

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]

One simple solution can be to put all employees’ working hours in a list and sort them on the start time. Then we can iterate through the list to find the gaps. Let’s dig deeper. Sorting the intervals of the above example will give us:

[1,3], [2,4], [6,8], [9,12]
We can now iterate through these intervals, and whenever we find non-overlapping intervals (e.g., [2,4] and [6,8]), we can calculate a free interval (e.g., [4,6]). This algorithm will take O(N * logN)O(N∗logN) time, where ‘N’ is the total number of intervals. This time is needed because we need to sort all the intervals. The space complexity will be O(N)O(N), which is needed for sorting. Can we find a better solution?

Using a Heap to Sort the Intervals
One fact that we are not utilizing is that each employee list is individually sorted!

How about we take the first interval of each employee and insert it in a Min Heap.
This Min Heap can always give us the interval with the smallest start time. Once we have the smallest start-time interval, we can then compare it with the next smallest start-time interval (again from the Heap) to find the gap.
This interval comparison is similar to what we suggested in the previous approach.
Whenever we take an interval out of the Min Heap, we can insert the same employee’s next interval.
This also means that we need to know which interval belongs to which employee.

Time Complexity
The above algorithm’s time complexity is O(N*logK), where ‘N’ is the total number of intervals,
and ‘K’ is the total number of employees. This is because we are iterating through the intervals only once
(which will take O(N)O(N)), and every time we process an interval, we remove (and can insert) one interval in the Min Heap,
(which will take O(logK). At any time, the heap will not have more than ‘K’ elements.

Space Complexity
The space complexity of the above algorithm will be O(K) as at any time, the heap will not have more than ‘K’ elements.
"""


from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval  # interval representing employee's working hours
        self.employee_index = employee_index  # index of the list containing working hours of this employee
        self.interval_index = interval_index  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, min_heap = [], []

    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    prev_interval = min_heap[0].interval
    while min_heap:
        queue_top = heappop(min_heap)  # the smallest
        # if previousInterval is not overlapping with the next interval,
        # insert a free interval
        if prev_interval.end < queue_top.interval.start:
            result.append(Interval(prev_interval.end, queue_top.interval.start))
            prev_interval = queue_top.interval

        else:  # overlapping intervals, update the previousInterval if needed.
            if prev_interval.end < queue_top.interval.end:
                prev_interval = queue_top.interval

        # if there are more intervals available for the same employee, add their next interval
        employee_schedule = schedule[queue_top.employee_index]
        if len(employee_schedule) > queue_top.interval_index + 1:
            heappush(min_heap, EmployeeInterval(employee_schedule[queue_top.interval_index + 1],
                                                queue_top.employee_index,
                                                queue_top.interval_index + 1))

    return result


def main():
    input1 = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end="")
    for interval in find_employee_free_time(input1):
        interval.print_interval()
    print()

    input2 = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end="")
    for interval in find_employee_free_time(input2):
        interval.print_interval()
    print()

    input3 = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end="")
    for interval in find_employee_free_time(input3):
        interval.print_interval()
    print()


main()
