from leetcode_classes import ListNode

class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        return []

if __name__ == '__main__':
    sol = Solution()
    test = [ListNode(1),
            ListNode(2),
            ListNode(3),
            ListNode(4),
            ListNode(5)]
    ans = sol.reverseList(test)
    for node_test in test:
        print(node_test, node_test.next)