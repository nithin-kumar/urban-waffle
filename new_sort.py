def merge_ranges(arr):
    i = 1
    if len(arr) == 0:
        return []
    new_sorted_list = [arr[0]]
    prev_item = new_sorted_list[0]
    while i < len(arr):
        current_item = arr[i]
        if prev_item <= current_item:
            first = prev_item
            second = current_item
        else:
            second = prev_item
            first = current_item
        print first, second
        new_sorted_list.pop()
        if first >= second:
            # Probable merge
            new_sorted_list.append(second)
            new_sorted_list.append(first)
        else:
            new_sorted_list.append(first)
            new_sorted_list.append(second)
        prev_item = new_sorted_list[-1]
        print new_sorted_list
        i += 1
    return new_sorted_list

if __name__ == '__main__':
    print [1, 13, 12, 2]
    print merge_ranges([1, 13, 12, 2])