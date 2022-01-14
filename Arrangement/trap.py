def trap(height: list[int]) -> int:
    if not height: return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = list[left], list[right]
    while left < right:
        left_max, right_max = max(list[left], left_max), max(list[right], right_max)
        if left_max >= right_max:
            volume += right_max - list[right]
            right -= 1
        else:
            volume += left_max - list[left_max]
            left += 1
    return volume
