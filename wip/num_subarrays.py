'''
Let lefts[i] be the number of valid subarrays ending with arr[i], and rights[i] the ones 
beginning with arr[i], then subarrays[i] = lefts[i] + rights[i] + 1 (plus one because a 
subarray that contains only arr[i] is valid too).

Now, calculating rights[i] is the same as calculating lefts[i] of arr.reverse().

Test cases:

var test_1 = [3, 4, 1, 6, 2];
var expected_1 = [1, 3, 1, 5, 1];
var output_1 = countSubarrays(test_1);
check(expected_1, output_1);

var test_2 = [2, 4, 7, 1, 5, 3];
var expected_2 = [1, 2, 6, 1, 3, 1];
var output_2 = countSubarrays(test_2);
check(expected_2, output_2);
'''
def count_subarrays(arr: list[int]) -> list[int]:
    '''
    O(n)
    '''
    # stack to store indexes of arr to compare against current.
    # bottom of stack, if any, is index of max(arr[:i]), the greatest yet
    stack = []

    # count subarrays that end with arr[i]
    # by checking valid subarrays from left of arr
    lefts = [0 for _ in arr]
    # O(n)
    for i in range(len(arr)):
        # if top of stack (decreasing previous indexes) is less than current,
        # discard it as it's useless against current, and check next
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        
        # if stack is not empty, top is index of left-most greater number than current arr[i]
        if stack:
            lefts[i] += i - stack[-1] - 1
        # if stack is empty, current arr[i] is max(arr[:i + 1]), the greatest yet
        else:
            lefts[i] += i

        # push current index to stack to be compared against next
        stack.append(i)
    
    # reset stack
    stack = []

    # now count subarrays that begin with arr[i]
    # by checking valid subarrays from right of arr by reversing indexes
    rights = [0 for _ in arr]
    # O(n)
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()

        if stack:
            rights[i] += stack[-1] - i - 1
        else:
            rights[i] += len(arr) - 1 - i
        
        stack.append(i)
    
    return [lefts[i] + rights[i] + 1 for i in range(len(arr))]


def count_subarrays(arr):
  n = len(arr)
  res = [1] * n
  stack = [-1]
  #left
  for i in range(n):
    while len(stack) > 1 and arr[stack[-1]] < arr[i]:
      stack.pop()
    res[i] += i - stack[-1] - 1
    stack.append(i)
  
  # from right
  stack = [n]
  for i in range(n - 1, -1, -1):
    while len(stack) > 1 and arr[stack[-1]] < arr[i]:
      stack.pop()
    res[i] += stack[-1] - i - 1
    stack.append(i)
  return res    