import numpy

def arrays(arr):
    # return numpy.array(list(reversed(arr)), float)
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
