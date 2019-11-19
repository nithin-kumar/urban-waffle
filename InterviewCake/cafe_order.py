def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    i = 0
    j = 0
    for k in range(len(served_orders)):
        if i < len(take_out_orders) and served_orders[k] == take_out_orders[i]:
            i += 1
        elif j < len(dine_in_orders) and served_orders[k] == dine_in_orders[j]:
            j += 1
        else:
            return False
    print i, len(take_out_orders)
    print j, len(dine_in_orders)
    if i != len(take_out_orders) or j != len(dine_in_orders):
        return False
    return True

if __name__ == '__main__':
    print is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])