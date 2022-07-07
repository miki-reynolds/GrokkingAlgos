'''
Instead of doing 2sum, 3sum, 4sum, etc, how do we solve a k-sum problem?
We want unique elements, no duplicates.
'''


def k_sum(array, k, start, target, k_array, result):
    if k != 2:
        for i in range(start, len(array) - k + 1):
            if i > start and array[i] == array[i-1]:
                continue
            k_array.append(array[i])  # add the first (k-2) elements in at each round
            k_sum(array, k-1, i+1, target - array[i], k_array, result)
            k_array.pop()  # pop all in at each round
        return  # finish everything in recursion before jump down to the next section

    #  base case when k = 2 (2sum), we could even have a modular function for this for readability (search_pairs)
    left, right = start, len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            # append k-elements to result array by using list concat
            result.append(k_array + [array[left], array[right]])
            left += 1
            right -= 1
            while left < right and array[left] == array[left-1]:
                left += 1  # skip same element to avoid duplicates
            while left < right and array[right] == array[right+1]:
                right -= 1  # skip same element to avoid duplicate triplets
        # we need a pair with a bigger sum
        elif current_sum < target:
            left += 1
        # we need a pair with a smaller sum
        else:
            right -= 1


def four_sum(array, target):
    array.sort()
    result = []
    k_array = [] # temp array to hold (k-2) elements before we get to base k=2
    k_sum(array, 4, 0, target, k_array, result)

    return result


def main():
    print(four_sum([4, 1, 2, -1, 1, -3], 1))  # [-3, -1, 1, 4], [-3, 1, 1, 2]
    print(four_sum([2, 0, -1, 1, -2, 2], 2))  # [-2, 0, 2, 2], [-1, 0, 1, 2]


main()

