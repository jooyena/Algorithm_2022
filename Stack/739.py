def DailyTemperature(weathers: list[int]):
    result = []

    for i in weathers:
        count = 0
        stack = weathers[i:]
        while stack:
            if i > stack.pop():
                count += 1
                return
        result.append(count)


def DailyTemperature(weathers: list[int]):
    result = []
