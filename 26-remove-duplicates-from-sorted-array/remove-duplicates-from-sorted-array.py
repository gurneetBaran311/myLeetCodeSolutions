class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0   # pointer which maintains position where we need to move the unique element
        i = 0
        while i < len(nums):
            if nums[i] > nums[x]:
                x = x + 1
                nums[x] = nums[i]
            i+=1    
        return x+1 # since we have x unique elements and index starts from 0
