
"""
Write a method that takes an array of characters and reverses 
the letters in place.


Why an array of characters instead of a string?

The goal of this question is to practice manipulating strings 
in place. Since we're modifying the input, we need a mutable  
type like an array, instead of Java's immutable strings.
"""
import unittest


def reverse(chars):
    
    loop_length = int(len(chars)/2)
    left, right = 0, len(chars) - 1
    
    for i in range(0, loop_length):
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp
        
        left += 1
        right -= 1



# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)
