"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    
    # Example: fib of 9 = fib of 8 + fib of 7
    # Exit loop when it is at 0. Gotta know the first two numbers to get the rest.
    
    if position <= 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
