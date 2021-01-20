"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Algorithm: using the 'sliding window technique'
        # For a variable called left, the index of the day the stock is sold
        # It should traverse the list from the first index until lastIndex - 1
        # and for right another variable, right will be the index of a day in the future when the stack is sold.
        # The goal is to find the value of the difference between the stock value at day 'right' and the one at day 'left'
        # If that value is negative, increment left. Otherwise, compare it to the current max_profit and increment right.
        # return max_profit.
        
      
        left, right = 0, 1
        max_profit = 0
        
        while(left < len(prices) - 1):
        
            profit = prices[right] - prices[left]
            
            if profit > 0:
                max_profit = max(max_profit, profit)
                right += 1
                  
                if right == len(prices): 
                    return max_profit 
            else:
                left += 1
                right = left + 1
                  
        return max_profit
      
