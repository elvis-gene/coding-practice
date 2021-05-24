"""
Latin Square

Given an n by n matrix of letters matrix, return whether there are exactly n different letters that appear in the matrix and each letter appears exactly once in each row and exactly once in each column.

Constraints

1 ≤ n ≤ 250 where n is the number of rows and columns in matrix
Example 1
Input
matrix = [
    ["a", "b", "c"],
    ["c", "a", "b"],
    ["b", "c", "a"]
]
Output
True
Explanation
There are 3 different letters and each letter appears exactly once in each row and column.

Example 2
Input
matrix = [
    ["a", "b", "c"],
    ["d", "a", "a"],
    ["b", "b", "a"]
]
Output
False
Explanation
There are 4 different letters, and also "a" and "b" appear twice in the same row.
"""

class Solution:
    def solve(self, matrix):
        
        colum_letters = []
        row_letters = []
        letters = set()

        for row_count, row in enumerate(matrix):
            
            for l in range(len(row)):
                letters.add(row[l]) 

                # Check columns
                if matrix[l][row_count] in colum_letters:
                    return False
                else:
                    colum_letters.append(matrix[l][row_count])

                # Check rows
                if row[l] in row_letters:
                    return False
                else:
                    row_letters.append(row[l])
            row_letters = []
            colum_letters = []

        return len(letters) == len(matrix)
