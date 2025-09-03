class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [ch.lower() for ch in s if ch.isalnum()]
        slow = 0
        fast = len(t) - 1
        while slow < fast:
            if t[slow] != t[fast]:
                return False
            slow+=1
            fast-=1
        return True    
            