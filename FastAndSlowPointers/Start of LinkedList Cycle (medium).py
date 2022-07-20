"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

Solution
If we know the length of the LinkedList cycle, we can find the start of the cycle through the following steps:
Take two pointers. Let’s call them pointer1 and pointer2.
Initialize both pointers to point to the start of the LinkedList.
We can find the length of the LinkedList cycle using the approach discussed in  LinkedList Cycle. Let’s assume that the length of the cycle is ‘K’ nodes.
Move pointer2 ahead by ‘K’ nodes.
Now, keep incrementing pointer1 and pointer2 until they both meet.
As pointer2 is ‘K’ nodes ahead of pointer1, which means, pointer2 must have completed one loop in the cycle when both pointers meet. Their meeting point will be the start of the cycle.

We can use the algorithm discussed in LinkedList Cycle to find the length of the cycle and then follow the above-mentioned steps to find the start of the cycle.

Time Complexity
As we know, finding the cycle in a LinkedList with ‘N’ nodes and also finding the length of the cycle requires O(N)O(N). Also, as we saw in the above algorithm, we will need O(N)O(N) to find the start of the cycle. Therefore, the overall time complexity of our algorithm will be O(N)O(N).

Space Complexity
The algorithm runs in constant space O(1).
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    slow, fast = head, head
    cycle_length = 0

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            cycle_length = find_cycle_length(slow)
            break

    pointer1, pointer2 = head, head
    # move pointer2 ahead 'cycle_length' nodes
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1

    # As pointer2 is ‘K’ nodes ahead of pointer1,
    # which means, pointer2 must have completed one loop in the cycle when both pointers meet.
    # Their meeting point will be the start of the cycle.
    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def find_cycle_length(slow):
    current = slow
    cycle_length = 0

    while True:
        current = current.next
        cycle_length += 1

        if current == slow:
            break

    return cycle_length


# Explanation: https://leetcode.com/problems/linked-list-cycle-ii/discuss/1701055/JavaC%2B%2BPython-best-explanation-ever-happen's-for-this-problem
def detect_cycle(self, head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: break
    else:  # if not (fast and fast.next): return None
        return None

    while head != slow:
        head, slow = head.next, slow.next
    return head



def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
