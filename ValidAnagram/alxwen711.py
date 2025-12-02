class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        b = [0]*26
        for i in s:
            a[ord(i)-97] += 1
        for j in t:
            b[ord(j)-97] += 1
        return a == b
        