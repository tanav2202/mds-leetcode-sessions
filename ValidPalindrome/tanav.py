import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        s= s.replace(" ", "")
        
        if s == s[::-1]:
            return True
        else: 
            return False