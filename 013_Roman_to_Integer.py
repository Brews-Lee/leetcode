class Solution:
    def romanToInt(self, s: str) -> int:
        def turn_to_numbers(roman: str) -> list[int]:
            nums = list()
            for char in roman:
                if char == "I":
                    nums.append(1)
                elif char == "V":
                    nums.append(5)
                elif char == "X":
                    nums.append(10)
                elif char == "L":
                    nums.append(50)
                elif char == "C":
                    nums.append(100)
                elif char == "D":
                    nums.append(500)
                elif char == "M":
                    nums.append(1000)
            return nums
        nums = turn_to_numbers(s)

        result = 0
        i = 0
        for num in nums:
            if i >= len(nums):
                break
            if i == len(nums) - 1:
                result += nums[len(nums) - 1]
                break
            # Next number is the same
            if nums[i] == nums[i + 1]:
                if i != len(nums) - 2 and nums[i] == nums[i + 2]:
                    result += 3 * nums[i]
                    i += 3
                    continue
                else:
                    result += 2 * nums[i]
                    i += 2
                    continue
            # Next number is larger
            elif nums[i] < nums[i + 1]:
                result += nums[i + 1] - nums[i]
                i += 2
                continue
            # Next number is smaller
            else:
                result += nums[i]
            i += 1
        return result

print(Solution().romanToInt("MCMXCVI"))