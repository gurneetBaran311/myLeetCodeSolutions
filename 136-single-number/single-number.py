class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using XOR approach as XOR cancels out duplicates. a^a = 0 and a^1=a
        result = 0
        for num in nums:
            result^= num
        return result    

                
