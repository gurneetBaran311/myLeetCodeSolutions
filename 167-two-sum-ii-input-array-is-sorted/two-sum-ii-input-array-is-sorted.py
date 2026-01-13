class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            total_sum = nums[i] + nums[j]

            if total_sum == target:
                return [i+1, j+1]

            i, j = (i + 1, j) if total_sum < target else (i, j - 1)