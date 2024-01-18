class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = 0
        for num in nums:
            j = 0
            for second_num in nums:
                if i == j:
                    j += 1
                    continue
                if num + second_num == target:
                    return [i, j]
                j += 1
            i += 1