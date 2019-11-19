def merge_ranges(meetings):
    i = 1
    if len(meetings) == 0:
        return []
    new_meeting_list = [meetings[0]]
    prev_meeting = new_meeting_list[0]
    while i < len(meetings):
        current_meeting = meetings[i]
        if prev_meeting[0] <= current_meeting[0]:
            first = prev_meeting
            second = current_meeting
        else:
            second = prev_meeting
            first = current_meeting
        print first, second
        new_meeting_list.pop()
        if first[1] >= second[0]:
            # Probable merge
            
            if second[1] >= first[1]:
                new_meeting_list.append((first[0], second[1]))
            else:
                new_meeting_list = [(first[0], first[1])]
        else:
            new_meeting_list.append(first)
            new_meeting_list.append(second)
        prev_meeting = new_meeting_list[-1]
        print new_meeting_list
        i += 1
    return new_meeting_list

if __name__ == '__main__':
    print merge_ranges([(5, 8), (1, 4), (6, 8)])