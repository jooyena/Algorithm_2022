import collections


def isPalindrome(head: list) -> bool:
    q: collections.deque = collections.deque

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


# Runner를 사용한 풀이
def isPalindrome(head: list) -> bool:
    rev = None
    slow = fast = head

    # 러너를 이용해 역순 구성
    # !! 동일 참조 주의할 것 !!
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
