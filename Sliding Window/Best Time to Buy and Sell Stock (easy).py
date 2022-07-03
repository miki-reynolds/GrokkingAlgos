'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

e.g.
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

e.g.
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''


def max_profit(prices: list[int]) -> int:
    left = 0 # left is buy and right is sell.
    max_profit = 0

    for right in range(1, len(prices)):
        if prices[left] > prices[right]:
            left = right  # instead of incrementing left only by 1 to the 'right,' we set left = right because we already traverse to that point of right. We know it is the lowest in this if-case.
        max_profit = max(max_profit, prices[right] - prices[left])

    return max_profit


def main():
    print(max_profit([7,1,5,3,6,4]))
    print(max_profit([7,6,4,3,1]))


main()