def mergesort(input):
  if len(input) <= 1:
    return input

  pivot = len(input) // 2

  left = mergesort(input[:pivot])
  right = mergesort(input[pivot:])

  return merge(left,right)


def merge(l,r):
  n = len(l)
  m = len(r)
  i = 0
  j = 0
  output = []

  while i < n and j < m:
    if l[i] <= r[j]:
      output.append(l[i])
      i+=1
    else:
      output.append(r[j])
      j+=1

  if i < n:
    output += l[i:]
  if j < m:
    output += r[j:]

  return output


if __name__ == '__main__':
  input = [1,3,100,-1,-100,2]
  ans = mergesort(input)
  assert ans == [-100, -1, 1, 2, 3, 100], "check yo code"
  print(ans)