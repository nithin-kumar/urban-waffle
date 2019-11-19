def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result = []
    combinationSumHelper(result, candidates, 0, target, [])
    print result
def combinationSumHelper(result, candidates, sumSoFar, target, path):
    print 'combinationSumHelper(' + str(result) + ',' + str(candidates) + ',' + str(sumSoFar) + ',' + str(path) +')'
    if sumSoFar == target:
        print path
        result.append(list(path))
        return
    for i in range(len(candidates)):
        if sumSoFar + candidates[i] <= target:
            path.append(candidates[i])
            combinationSumHelper(result, candidates[i:], sumSoFar + candidates[i], target, path)
            path.pop()

if __name__ == '__main__':
    combinationSum([2,3,5, 1, 4], 5)
                        