import math
def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    if len(list_of_ints) < 3:
        raise Exception
        return
    window = [list_of_ints[0], list_of_ints[1], list_of_ints[2]]
    min_number = min(window)
    min_index = window.index(min_number)
    prod = reduce(lambda x, y: x*y, window)
    for i in range(3, len(list_of_ints)):
        if list_of_ints[i] > min_number:
            window[min_index] = list_of_ints[i]
            min_number = min(window)
            min_index = window.index(min_number)
            prod = max(prod, reduce(lambda x, y: x*y, window))
    return prod


print highest_product_of_3([-10, 1, 3, 2, -10])