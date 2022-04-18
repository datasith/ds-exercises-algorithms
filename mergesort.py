
def mergesort(nums):
  if len(nums) <= 1:
    return nums

  pivot = len(nums) // 2

  left = mergesort(nums[:pivot])
  right = mergesort(nums[pivot:])
  return merge(left,right)

def merge(l, r):
  i = 0
  j = 0
  output = []
  while i < len(l) and j < len(r):
    if l[i] <= r[j]:
      output.append(l[i])
      i += 1
    else:
      output.append(r[j])
      j += 1
  if i < len(l):
    output += l[i:]
  if j < len(r):
    output += r[j:]
  return output

if __name__ == "__main__":

  nums = [1,3,4,5,2,-81, 199, 3]

  print(mergesort(nums))