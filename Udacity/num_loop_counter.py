"""
Calculate the number of "loops" in a number.
A number has a loop when it has a closed circle when you draw it, so
6 has one loop, 1 has no loop and 8 has two loops.
So 2876 has three loops

"""

def loop_counter(num):
    num_and_value = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:0, 8:2, 9:1}

    counter = 0
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i].isdigit():
            counter += num_and_value.get(int(num_str[i]))

    return counter

counter = loop_counter(2876)
print(counter)
