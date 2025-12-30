class Solution:
    def strStr(self, h: str, needle: str) -> int:
        m, n = len(h), len(needle)
        if n > m:
            return -1
        for i in range(m - n + 1):
            if h[i : i + n] == needle:
                return i
        return -1
