class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        # for i in range(n):
        #     map[nums[i]] = i
        # for i in range(n):
        #     pairToFind = target - nums[i]
        #     if (pairToFind in map) and (map[pairToFind] != i):
        #         return [i, map[pairToFind]]

        for i,num in enumerate(nums):
            pairToFind = target - num
            if pairToFind in map:
                return [map[pairToFind],i]
            map[num] = i   
