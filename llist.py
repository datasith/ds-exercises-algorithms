class ListNode(object):
    def __init__(self, val: int, next: int=None) -> 'ListNode':
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{{val:{self.val}, next:{self.next}}}'

def list_to_llist(data: list) -> [ListNode]:
    out = []
    n = len(data)
    if n == 0:
        return []
    elif n == 1:
        return [ListNode(data[0], None)]
    data.append(None)
    for i in range(n):
        d = data[i]
        next = data[i+1]
        out.append(ListNode(d, next))
    return out

if __name__ == '__main__':
    node = ListNode(1)
    _ = range(5)
    _llist = list_to_llist(list(_))
    print(_llist)

        