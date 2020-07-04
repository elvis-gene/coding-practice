# A prime number is a number that only has two factors (itself and 1)

def is_prime(num: int) -> bool:
    if num < 2: return False
    elif num == 2: return True

    else:
        # No number is divisible by any number greater than its half (except itself)
        # So we will not bother diving with those numbers
        for i in range(3, int(num/2) + 1, 2):
            if num%i == 0: return False

        return True


assert(is_prime(1) is False)
assert(is_prime(-5) is False)
assert(is_prime(15) is False)
assert(is_prime(47) is True)
