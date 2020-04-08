# Elvis Gene
# Date: 2020 - 03 - 22

"""
The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string, or ")"
if that character appears more than once in the original string. Ignore capitalization
when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
Notes

Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

"""


def duplicate_encode(word):
    word = word.lower()

    if len(word) == 0:
        return ''

        # Alternatives
    #     if not word:
    #         return '';
    #     if word == '':
    #         return '';

    char_occur = dict()
    # Saving every character with its
    # number of occurrences in the string.
    for i in range(len(word)):
        char_occur[word[i] + str(i)] = word.count(word[i])  # There was a bug here as a dictionary
        # can't save duplicated keys.

    new_string = list()
    for key in char_occur:
        if char_occur.get(key) < 2:
            new_string.append('(')
        else:
            new_string.append(')')

    return str.join('', new_string)


print(duplicate_encode('din'))
print(duplicate_encode('recede'))
print(duplicate_encode('Success'))
print(duplicate_encode('(( @'))

# Test.assert_equals(duplicate_encode("din"), "(((")
# Test.assert_equals(duplicate_encode("recede"), "()()()")
# Test.assert_equals(duplicate_encode("Success"), ")())())", "should ignore case")
# Test.assert_equals(duplicate_encode("(( @"), "))((")
#
