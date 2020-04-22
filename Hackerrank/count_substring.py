def count_substring(string, sub_string):
    str_len = len(string)
    sub_len = len(sub_string)
    counter = 0

    for i in range(str_len):
        if string[i:i+sub_len] == sub_string:
            counter += 1

    return counter
    # return string.count(sub_string)
