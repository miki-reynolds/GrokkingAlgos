'''
Given an array, find the average of all  subarrays of ‘K’ contiguous elements in it.
'''


def find_averages_of_subarrays(k, arr):
  result = []
  window_sum, window_start = 0.0, 0
  for window_end in range(len(arr)):
    window_sum += arr[window_end]  # add the next element
    # slide the window, no need to slide if we've not hit the required window size of 'k'
    if window_end >= k - 1:
      result.append(window_sum / k)  # calculate the average
      window_sum -= arr[window_start]  # subtract the element going out
      window_start += 1  # slide the window ahead

  return result

def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]