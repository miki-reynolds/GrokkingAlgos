"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

e.g.
Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the
jobs are running at the same time i.e., during the time interval (2,4).

e.g.
Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.

e.g.
Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].

Solution
The problem follows the Merge Intervals pattern and can easily be converted to Minimum Meeting Rooms.
Similar to ‘Minimum Meeting Rooms’ where we were trying to find the maximum number of meetings happening at any time,
for ‘Maximum CPU Load’ we need to find the maximum number of jobs running at any time.
We will need to keep a running count of the maximum CPU load at any time to find the overall maximum load.

Time Complexity
The time complexity of the above algorithm is O(N*logN), where ‘N’ is the total number of jobs.
This is due to the sorting that we did in the beginning.
Also, while iterating the jobs, we might need to poll/offer jobs to the priority queue. Each of these operations can take O(logN).

Space Complexity
The space complexity of the above algorithm will be O(N), which is required for sorting.
Also, in the worst case, we have to insert all the jobs into the priority queue (when all jobs overlap) which will also take O(N) space.
The overall space complexity of our algorithm is O(N).
"""


from heapq import *


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end


def find_max_cpu_load(jobs):
    # sort the jobs by start time
    jobs.sort(key=lambda job: job.start)
    max_cpu_load, current_cpu_load = 0, 0
    min_heap = []
    # [[1, 4, 3], [2, 5, 4], [7, 9, 6]]
    for job in jobs:
        # remove all the jobs that have ended
        while len(min_heap) > 0 and job.start >= min_heap[0].end:
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)

        # add the current job into min_heap
        heappush(min_heap, job)
        current_cpu_load += job.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)

    return max_cpu_load


def main():
    print("Maximum CPU load at any time: " +
               str(find_max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
    print("Maximum CPU load at any time: " +
               str(find_max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
    print("Maximum CPU load at any time: " +
               str(find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))


main()

