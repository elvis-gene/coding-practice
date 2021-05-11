"""
You are given n people represented as an integer from 0 to n - 1, and a list of friends tuples, where person friends[i][0] and person friends[i][1] are friends.

Return whether everyone has at least one friend.

Constraints

m ≤ 100,000 where m is the length of friends
Example 1
Input
Visualize
n = 3
friends = [
    [0, 1],
    [1, 2]
]
Output
True
Explanation
Person 0 is friends with 1
Person 1 is friends with 0 and 2
Person 2 is friends with 1.
Example 2
Input
Visualize
n = 3
friends = [
    [0, 1]
]
Output
False
Explanation
Person 2 is not friends with anyone.
"""

class Solution:
    def solve(self, n, friends):
        
        # Someone has no friend if she/he is not in any of the lists

        people = []
        for f in friends:
            people.extend(f)

        is_friend = False
        count = 0

        for i in range(n):
            if i in people:
                count += 1
        
        return count == n
