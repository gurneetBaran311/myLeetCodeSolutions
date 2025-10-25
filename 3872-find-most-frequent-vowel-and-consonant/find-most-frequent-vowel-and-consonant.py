class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a','e','i','o','u'}
        map = {}
        kmax = cmax = 0
        for ch in s:
            map[ch] = map.get(ch,0)+1
            if ch in vowels:
                kmax = max(kmax,map[ch])
            else:
                cmax = max(cmax,map[ch])
        return kmax + cmax     

