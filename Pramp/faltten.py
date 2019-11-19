def flatten_array(map_):
  print map_
  out = {}
  q = [([], map_)]
  while len(q) != 0:
    item = q.pop(0)
    prefix = item[0]
    dictionary = item[1]
    for k,v in dictionary.items():
      if type(v) != type({}):
        if prefix == []:
          out[k] = v
        else:
          if k == '':
            out['.'.join(prefix)] = v
          else:
            out['.'.join(prefix) +'.'+ k] = v
      else:
        if k != '':
          prefix.append(k)
        q.append((list(prefix), v))
        if k != '':
          prefix.pop()
  return out



def flatten_array_recursive(map_, prefix, out):
  for k,v in map_.items():
    if type(v) != type({}):
        if prefix == '':
          out[k] = v
        else:
          if k == '':
            out[prefix] = v
          else:
            out[prefix +'.'+ k] = v
    else:
      if k and prefix != '':
        tmp = prefix + '.' + k
      elif k:
        tmp = k
      else:
        tmp = prefix
      flatten_array_recursive(v, tmp, out)

  return out



if __name__ == '__main__':
  dict_ = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }
  #print flatten_array(dict_)
  print flatten_array_recursive(dict_, '', {})