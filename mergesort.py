'''
input = [1,2,4,6,5,3]

  [1,2,4]     [6,5,3]
 [1] [2,4]   [6] [5,3]
    [2] [4]     [5] [3]



return [1,2,3,4,5,6]
'''

def merge_sort(nums):
  output = []
  if len(nums) <= 1:
    return nums
  
  mid = len(nums) // 2
  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])
  
  return merge(left, right)

def merge(left, right):
  i = 0
  j = 0
  merged = [0]*(len(left)+len(right))
  idx = 0
  
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged[idx] = left[i]
      idx+=1
      i += 1
    else:
      merged[idx] = right[j]
      idx+=1
      j += 1
  
  if i < len(left):
    merged[idx:] = left[i:]
  if j < len(right):
    merged[idx:] = right[j:]
  return merged
    
numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
print(merge_sort(numbers))