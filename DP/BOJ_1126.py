# N = 50개의 블록을 이용하여 높이가 같은 두 개의 탑을 만든다. 모든 블록을 사용할 필요는 없으며, 각 블록의 높이는 최대 50만이고, 모든 블록의 높이의 합이 50만 이하이다.
# 이때, 만들 수 있는 탑의 높이의 최댓값을 구하는 문제

def same_build(array: list, max: int, N:int) -> int:

    for i in array:
        sum+=top[i]
        