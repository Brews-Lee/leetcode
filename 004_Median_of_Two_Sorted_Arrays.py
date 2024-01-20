class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        # nums = sorted(nums)
        nums = sorted(nums1)

        if len(nums) % 2 == 1:
            median = nums[int(((len(nums) - 1) / 2))]
        elif len(nums) % 2 == 0:
            median1 = nums[int((len(nums)) / 2) - 1]
            median2 = nums[int((len(nums)) / 2)]

            median = (median1 + median2) / 2

        return median

print(Solution().findMedianSortedArrays([1, 3], [2, 4]))
