"""
Given a number n, return a list of all prime numbers smaller than or equal to n in ascending order.

Constraints

n ≤ 100,000
Example 1
Input
n = 3
Output
[2, 3]
Example 2
Input
n = 10
Output
[2, 3, 5, 7]
Example 3
Input
n = 20
Output
[2, 3, 5, 7, 11, 13, 17, 19]
"""

class Solution:
    def solve(self, n):
        
        # A prime number is a number only divisible by 1 and itself
        
        # Algorithm:
        # For each number less than n, check if it is prime

        primes = []
        is_prime = True

        for i in range(2, n+1):
            
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            
            if is_prime:
                primes.append(i)
                
            is_prime = True

        return primes
