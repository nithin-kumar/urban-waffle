def flip(arr, k):
  for i in range(k - 1):
    arr[i], arr[k - i - 1]  = arr[k - i - 1], arr[i]
  return arr

def max_(arr):
  max_elem = 0
  for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
      max_elem = i
  return max_elem + 1

def pancake_sort(arr):
  window_len = len(arr)
  while window_len >= 0:
    max_index = max_(arr[0: window_len])
    # arr[0], arr[max_] = arr[max_], arr[0]
    flip(arr, max_index)
    flip(arr, window_len)
    window_len -= 1
  return arr

if __name__ == '__main__':
  #print flip([1, 2, 3, 4], 4)
  #print max_([5, 6, 3, 8])
  print pancake_sort(flip([1, 2, 3, 4], 4))
