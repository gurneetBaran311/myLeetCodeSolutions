class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = 0 # to maintain
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[x],nums[i] = nums[i],nums[x]
                x+=1
        return nums    

        """
        Do not return anything, modify nums in-place instead.
        """
        