def reverseList(l1: list[int]):
    for i in l1.next:
        rev, rev.next = i, rev
    return rev


# 책 재귀 이용

def reverseList(head: list) -> list:
    def reverse(node: list, prev: list = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


# 책 반복문
def reverseList(head: list) -> list:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev
