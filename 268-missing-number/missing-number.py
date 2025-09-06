class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        partial_sum = 0
        for i in range(n):
            partial_sum = partial_sum + nums[i]
        return expected_sum - partial_sum
