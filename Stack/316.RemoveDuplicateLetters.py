import collections

import Stack


def RemoveDuplicate(letter: str):
    # 집합으로 정렬 - > 집합은 중복이 제거된 자료형
    # 접미사와 집합과 비교했을 때 같다면 분리 다르다면 그 다음으로 진행
    for char in sorted(set(letter)):
        suffix = letter[letter.index(char):]
        # 같다면 분리
        if set(letter) == set(suffix):
            return char + RemoveDuplicate(suffix.replace(suffix.replace(char, '')))


def RemoveDuplicate(letter: str):
    counter, seen, stack = collections.Counter(letter), set(), []

    for char in letter:
        counter[char] -= 1

        if char in stack:
            continue

        # 뒤에 붙일 문자가 남아있다면
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

        return ''.join(stack)
