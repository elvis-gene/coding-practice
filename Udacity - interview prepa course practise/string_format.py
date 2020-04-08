def str_format(string, arg1, arg2):
    output = string.format(arg1, arg2)
    print(output)

    
str_format('Hello {0} {1}', 'Mr.', 'X')
str_format('{1}_{0}', '{1}', '{0}')
