def swapNodePairs(node: list[int]) -> list[int]:
    while node:
        node, node.next = node.next, node
        node = node.next.next
    return node


def swapNodePairs(node: list[int]) -> list[int]:
    root = prev = list(0)
    prev.next = node

    while node and node.next:
        b = node.next
        node.next = b.next
        b.next = node

        prev.next = b

        node = node.next
        prev = prev.next.next
    return root.next



