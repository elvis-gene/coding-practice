"""
Wolves of Wall Street

Given a list of integers prices representing the stock prices of a company in chronological order, return the maximum profit you could have made from buying and 
selling that stock any number of times.

You must buy before you can sell it. But you are not required to buy or sell the stock.

Constraints

0 ≤ n ≤ 100,000 where n is the length of prices
Example 1
Input
prices = [1, 5, 3, 4, 6]
Output
7
Explanation
We can buy at 1, sell at 5, buy at 3, and sell at 6.
"""

class Solution:
    def solve(self, s):
        
        # Using a stack
        liste = []

        for c in s:
            if not liste or liste[-1] == c:
                liste.append(c)
            elif liste[-1] != c:
                liste.pop()

        return len(liste)
