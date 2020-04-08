"""
Implement a function that adds two numbers together and returns
their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.
"""


def add_binary(a, b):
    som = a + b
    num = som

    if num % 2 == num:
        return str(num)

    sequence = list()

    while num % 2 != num:
        sequence.append(str(num % 2))
        num = int(num / 2)

        # To add the last number to the list
        # as it won't be added at the next run
        # since the loop check will be false.
        if num % 2 == num:
            sequence.append(str(num))

    # Reverse list
    sequence.reverse()

    return str.join('', sequence)


print(add_binary(51, 12))
print(add_binary(1, 0))
print(add_binary(1, 1))


# Another more efficient solution
def sum_binary(a, b):
    return bin(a+b)[2:]


print(sum_binary(51, 12))
print(sum_binary(1, 0))
print(sum_binary(1, 1))

# Test.assert_equals(add_binary(1,1),"10")
# Test.assert_equals(add_binary(0,1),"1")
# Test.assert_equals(add_binary(1,0),"1")
# Test.assert_equals(add_binary(2,2),"100")
# Test.assert_equals(add_binary(51,12),"111111")

