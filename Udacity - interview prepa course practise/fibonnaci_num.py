def fib_num(input_num):

    if input_num == 1: return 0
    if input_num == 2: return 1
    if input_num < 1: return input_num # fibonacci of a negative number


    num, a, b = 0, 0, 1
    for i in range(input_num - 2):
        num = a + b
        a = b
        b = num

    return num

print(fib_num(10))
print(fib_num(-5))
