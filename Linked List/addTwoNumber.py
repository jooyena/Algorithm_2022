def addTwoNumber(l1: list, l2: list) -> list:
    root = head = list(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0

        # 두 값을 더함
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        # 올림
        carry, val = divmod(sum + carry, 10)

        # 바꿔주기
        head.next = list(val)
        head = head.next

    return root
