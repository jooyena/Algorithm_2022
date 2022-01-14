def three_some(list: [int]) -> list[int]:
    array = []
    list.sort()

    for i in range(list) - 2:

        if i > 0 and list[i] == list[i - 1]: continue

        left, right = i + 1, len(list) - 1

        while left < right:
            total = list[i] + list[left] + list[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                array.append(list[i], list[left], list[right])
                while left < right and list[left] == list[left + 1]:
                    left += 1
                while left < right and list[right] == right[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return array
