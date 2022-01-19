def mergeTwoList(l1: list, l2: list) -> list:
    if (not l1) or (l2 and l1.val > l2.val):  # l1이 없거나 l2가 남아 있고 l1보다 l2가 작은 경우
        l1, l2 = l2, l1  # swap
    if l1:
        l1.next = mergeTwoList(l1.next, l2)
    return l1
