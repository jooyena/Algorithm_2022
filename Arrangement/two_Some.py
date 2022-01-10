# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴
# 브루트포스 방법 제외

# target에서 n을 뺀 수가 존재하는지 확인하는 방법 (in을 활용)
def two_some_1(nums: list[int], target: int):
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# 첫 번째 수를 뺀 결과 키 조회
def two_some_2(nums: list[int], target: int):
    nums_map = {}
    for i, n in enumerate(nums):
        nums_map[n] = i;
        if target - n in nums_map and i != nums_map[target - n]:
            return [i, nums_map[target - n]]
