def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    i = 0
    j = 0
    out = []
    while i < len(my_list) and j < len(alices_list):
        if my_list[i] <= alices_list[j]:
            out.append(my_list[i])
            i += 1
        else:
            out.append(alices_list[j])
            j += 1
    print my_list, alices_list
    print i, j
    if len(my_list) > i:
        out += my_list[i:]
    if len(alices_list) > j:
        out += alices_list[j:]

    return out

if __name__ == '__main__':
    print merge_lists([2, 4, 6, 8], [1, 7])