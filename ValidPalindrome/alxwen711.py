class Solution:
    def isalphanumeric(self,x):
        c = ord(x)
        return (ord("a") <= c <= ord("z")) or (ord("A") <= c <= ord("Z")) or (ord("0") <= c <= ord("9"))

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        lp = 0
        rp = n-1
        while lp < rp:
            while lp < n:
                if self.isalphanumeric(s[lp]): break
                lp += 1
            while rp >= 0:
                if self.isalphanumeric(s[rp]): break
                rp -= 1
            if lp >= rp: return True
            if s[lp].lower() != s[rp].lower(): return False
            lp += 1
            rp -= 1
        return True
        