class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers)-1
        while(i<j):
            sum1 = numbers[i] + numbers[j]
            if  sum1 == target:
                return [i+1,j+1]   
            if sum1<target:
                i+=1    
            else:    
                j-=1