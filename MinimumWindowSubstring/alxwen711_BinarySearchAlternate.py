"""
This is an alternate (albleit significantly slower) solution to Minimum Window Substring.

Suppose the smallest viable substring is length x. Then there must exist substrings of length
x+1, x+2, x+3, ... all the way to len(s) that also contain every letter in string t.

Knowing this we can binary search for the shortest possible length from 1 to len(s).

Bruteforcing all possible substrings of a specific length can be done through a basic
sliding window technique (for a length n, insert the first n characters, then repeatedly add 1, remove 1
until the entire string has been processed). This process takes place in the helper function f, and takes
O(n) time. Since O(log n) calls are made to function f for the binary search, the entire algorithm takes
O(n log n) time to complete, as compared to the more optimal solution that takes O(n) time to complete.
In actual practice the optimized solution took roughly 95ms on Leetcode to complete whereas this solution
takes nearly 4 seconds.
"""

class Solution:
    def f(self,s,profile,x):
        n = len(s)
        p = [0]*128
        for ii in range(x-1):
            p[ord(s[ii])] += 1
        for j in range(x-1,n):
            p[ord(s[j])] += 1
            flag = True
            for l in range(128):
                if profile[l] > p[l]:
                    flag = False
                    break
            if flag: return j-x+1
            p[ord(s[j-x+1])] -= 1
        return -1

    def minWindow(self, s: str, t: str) -> str:
        # lt binary method
        low = len(t)
        high = len(s)
        if low > high: return ""
        
        # generate profile of t
        profile = [0]*128
        for i in t:
            profile[ord(i)] += 1

        # run the binary search
        while high-low > 1:
            mid = (low+high)//2
            if self.f(s,profile,mid) != -1: high = mid
            else: low = mid
        
        ans = self.f(s,profile,low)
        if ans != -1: return s[ans:ans+low]
        
        ans = self.f(s,profile,high)
        if ans != -1: return s[ans:ans+high]
        
        return ""