def climbingStaircase(n, k):
    result = []
    climbingStaircaseHelper(n, k, result, [], 0)
    return result

def climbingStaircaseHelper(n, k, result, chosen, current_stair):
    #print 'climbingStaircaseHelper(' + str(n) + ',' + str(chosen) + ',' + str(current_stair) + ')'
    if n == 0:
        result.append(list(chosen))
        return
    for i in range(1, k + 1):
        # Choose
        if n >= 0:
            chosen.append(i)
            # Explore
            climbingStaircaseHelper(n - i, k, result, chosen, current_stair + i)
            chosen.pop()

print climbingStaircase(4, 2)