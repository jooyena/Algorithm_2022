def reverseLinkedList(head: list, start: int, fin: int) -> list[int]:
    node, prev = head, None
    cnt: int = 0

    if head is None or (start == fin - 1):
        return None

    while head or cnt == fin:
        if cnt != start:
            node = node.next
            continue

        node, node.next = node.next, prev
        prev, head = node, prev

    return prev


# 책 풀이

def reverseLinkedList(head: list, m: int, n: int) -> list[int]:
    if not head or m == n:
        return head

    root = start = list(None)
    root.next = head

    for _ in range(m - 1):
        root = root.next
    end = start.next

    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp

    return root.next


print(reverseLinkedList([1, 2, 3, 4, 5], 2, 4))
