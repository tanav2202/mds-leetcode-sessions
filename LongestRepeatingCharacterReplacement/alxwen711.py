class Solution:
    # O(n) solution by using two pointer/sliding window and slight optimization
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        maxans = len(s)
        for i in range(maxans):
            if d.get(s[i]) == None:
                d[s[i]] = list()
            d[s[i]].append(i)
        
        # solve each specific character individually
        ans = 0
        for j in d.keys():
            ar = d[j]
            n = len(ar)
            back = 0
            for a in range(n):
                """
                length of segment testing: ar[a]-ar[back]+1
                number of specific letter in segment: a-back+1
                number of changes allowed: k
                """
                while (ar[a]-ar[back]+1)-(a-back+1) > k:
                    back += 1
                """
                number of free passes (letters not needed to change)
                will be a-back+1
                note: answer can be at most length of s
                """
                ans = max(ans,min(maxans,a-back+1+k))
        return ans