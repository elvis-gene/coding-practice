"""
Problem: Implement an algorithm to determine if a string has all unique characters.

Constraints:
Can we assume the string is ASCII?
Yes
Note: Unicode strings could require special handling depending on your language
Can we assume this is case sensitive?
Yes
Can we use additional data structures?
Yes
Can we assume this fits in memory?
Yes

Test Cases:
None -> False
'' -> True
'foo' -> False
'bar' -> True
"""

# Approach 1: Set length and String length comparison
class UniqueCharsSet(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)
      
 # Complexity:
# Time: O(n)
# Space: Additional O(n)


 # Approach 2: Hash Map Lookup     
class UniqueChars(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        chars_set = set()
        for char in string:
            if char in chars_set:
                return False
            else:
                chars_set.add(char)
        return True
      
# Complexity:
# Time: O(n)
# Space: Additional O(n)

    
# Approach 3: In place
# Assume we cannot use additional data structures, which will eliminate the fast lookup O(1) time provided by our hash map.  
class UniqueCharsInPlace(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        for char in string:
            if string.count(char) > 1:
                return False
        return True
      
# Algorithm Complexity:
# Time: O(n^2)
# Space: O(1)





%%writefile test_unique_chars.py
from nose.tools import assert_equal


class TestUniqueChars(object):

    def test_unique_chars(self, func):
        assert_equal(func(None), False)
        assert_equal(func(''), True)
        assert_equal(func('foo'), False)
        assert_equal(func('bar'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    unique_chars = UniqueChars()
    test.test_unique_chars(unique_chars.has_unique_chars)
    try:
        unique_chars_set = UniqueCharsSet()
        test.test_unique_chars(unique_chars_set.has_unique_chars)
        unique_chars_in_place = UniqueCharsInPlace()
        test.test_unique_chars(unique_chars_in_place.has_unique_chars)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
