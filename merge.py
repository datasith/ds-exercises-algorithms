def merge(left, right):
    i = 0
    j = 0
    merged = []
    
    left = list(filter(None, left))
    left = sorted(left)
    right = sorted(right)

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    if i < len(left):
        merged += left[i:]
    if j < len(right):
        merged += right[j:]
    return merged

if __name__ == '__main__':
    x = [1,2,3,None,None,None]
    y = [4,2,3]
    ans = merge(x,y)
    assert ans == [1,2,2,3,3,4]
    print(ans)