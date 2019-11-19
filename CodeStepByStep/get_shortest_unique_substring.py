from collections import defaultdict
def get_shortest_unique_substring(arr, str):
  def check_equality(map1, map2):
    if map1 == map2 :
      return True
    return False
  if str == "":
    return ""
  min_ = len(arr)
  max_ = len(str)
  src_ascii_map = defaultdict(int)
  for i in arr:
    src_ascii_map[ord(i)] += 1
  print src_ascii_map
  target_map = defaultdict(int)
  i = 0
  j = 0
  min_str = ""
  min_str_len = 99999
  while j < len(str):
    if ord(str[j]) in src_ascii_map:
      target_map[ord(str[j])] += 1
    if check_equality(src_ascii_map, target_map):
      if j - i  + 1 < min_str_len:
        min_str = str[i : j + 1]
        min_str_len = j - i  + 1
      if j - i  + 1 == min_:
        return min_str
      while check_equality(target_map, src_ascii_map):
        if ord(str[i]) in target_map:
          target_map[ord(str[i])] -= 1
          if target_map[ord(str[i])] == 0:
            del target_map[ord(str[i])]
          if j - i + 1 < min_str_len:
            min_str = str[i : j + 1]
            min_str_len = j - i + 1
          if j - i  + 1 == min_:
            return min_str
        i += 1
    j +=1
  return min_str


#print get_shortest_unique_substring(["A","B","C"], "ABCBECODEBANCDDD")

#print get_shortest_unique_substring(["A","B","C"], "ADOBECODEBANCDDD")
print get_shortest_unique_substring(["x","y","z"], "xyyzyzyx")

#print get_shortest_unique_substring(['a', 'a'], 'aa')