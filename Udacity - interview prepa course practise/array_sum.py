"""
Calculate the sum of an array which contains integers
and other arrays with integers.
For example:

array_sum([1,2,[3,4,[5]]])
would return 15.
"""


def sum(array):
    # print(array.size())

    array = str(array)
    array = array.replace('[','').replace(']','').split(',')

    # String.strip()
    sum = 0
    for num in array:
        if num.strip().isdigit():
            sum += int(num)

    return sum


print(sum([1,2,[3,4,[5]]]))
