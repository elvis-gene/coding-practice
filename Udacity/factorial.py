def factorial(num: int) -> int:
    if num == 0: return 1

    ans = 1
    while(num >= 1):
        ans = ans * num
        num = num - 1
    return ans

print(factorial(5))


# Using recursion
def factorial_rec(num : int) -> int:
    if num < 2: return num

    return factorial_rec(num - 1) + factorial_rec(num - 2)

print(factorial_rec(5))
