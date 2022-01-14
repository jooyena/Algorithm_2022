def partition(list: list[int]) -> list[int]:
    out = []
    p = 1
    for i in range(0, len(list)):
        p = p * list[i]
        out.append(p)
    p = 1
    for i in range(len(list) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * out[i]
    return out
