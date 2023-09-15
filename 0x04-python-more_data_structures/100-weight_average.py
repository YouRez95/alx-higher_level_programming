#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_of_numerator = 0
    divide = 0

    if len(my_list) == 0:
        return 0
    for i in my_list:
        mult = i[0]*i[1]
        sum_of_numerator += mult
        divide += i[1]

    result = sum_of_numerator / divide
    return result
