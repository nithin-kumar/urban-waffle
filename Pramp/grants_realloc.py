def find_grants_cap(grantsArray, newBudget):
  grantsArray.sort(reverse=True)
  print grantsArray
  if len(grantsArray) == 0:
    return 0
  if len(grantsArray) == 1:
    return newBudget
  poi = -1
  total_grants = sum(grantsArray)
  tmp = 0
  for i in range(len(grantsArray)):
    tmp += grantsArray[i]
    if (i + 1) * grantsArray[i] + (total_grants - tmp) <= newBudget:
      poi = i
      break
  if poi == -1:
    return newBudget / float(len(grantsArray))
  remaining_sum = 0
  for j in range(poi,  len(grantsArray)):
    remaining_sum += grantsArray[j]
  if poi != 0:
    return (newBudget - remaining_sum) / float(poi)
 
  return newBudget - (remaining_sum - grantsArray[0])



print find_grants_cap([2,100,50,120,167], 500)