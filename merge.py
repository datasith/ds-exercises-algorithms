class Solution(object):
    def merge(self, x: list, y: list) -> list:
        left = right = 0
        output = []

        x = list(filter(None, x))
        x, y =  sorted(x), sorted(y)
        n, m = len(x), len(y)
        while True:
            if left < n and right < m:
                if x[left] <= y[right]:
                    output.append(x[left])
                    left += 1
                else:
                    output.append(y[right])
                    right += 1
            elif left < n:
                output.append(x[left])
                left += 1
            elif right < m:
                output.append(y[right])
                right += 1
            else:
                break
        return output

if __name__ == '__main__':
    sol = Solution()
    x = [1,2,3,None,None,None]
    y = [4,2,3]
    ans = sol.merge(x,y)
    print(ans)