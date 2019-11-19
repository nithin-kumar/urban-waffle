def decodeVariations(S):
  result = []
  decodeVariationsHelper(S, [], result, '')
  print result
  return len(result)
  
  
def decodeVariationsHelper(S, chosen, result, recursion_space):
  print recursion_space + 'decodeVariationsHelper(' + S + ',' + str(chosen) + ')'
  if len(S) == 0:
    print recursion_space + str(chosen)
    result.append(list(chosen))
    return 
  for i in range(len(S)):
    tmp = int(S[:i+1])
    if int(tmp) > 0 and int(tmp) < 27:
      chosen.append(tmp)
      recursion_space += ' '
      decodeVariationsHelper(S[i+1:], chosen, result, recursion_space)
      recursion_space = recursion_space[:-1]
      chosen.pop()


if __name__ == '__main__':
  decodeVariations('1262')