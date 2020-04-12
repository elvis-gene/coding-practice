def is_prime(num: int) -> bool:
    if num < 2: return False
    elif num == 2: return True

    else:
        # No number is divisible by any number
        # (except divided by itself) greater than its half
        for i in range(3, int(num/2) + 1, 2):
            if num%i == 0: return False

        return True


assert(is_prime(1) is False)
assert(is_prime(-5) is False)
assert(is_prime(15) is False)
assert(is_prime(47) is True)
