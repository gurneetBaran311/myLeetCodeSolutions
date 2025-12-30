class Solution:
    def strStr(self, h: str, needle: str) -> int:
        n,m = len(h),len(needle)
        if m ==0:
            return 0
        for i in range(n-m+1):
            j = 0
            while j<m and h[i+j]==needle[j]:
                j+=1
            if j==m:
                return i
        return -1            
            
