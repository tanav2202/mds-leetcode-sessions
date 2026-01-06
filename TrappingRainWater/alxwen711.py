"""
General idea of this solution is to work from the bottom up,
keep track of the left and right most endpoints that are of at least height
(1,2,3,4...100000) and how many columns are filled still (ie. of at least height
1,2,3,4,...,100000). Then the amount of water at each level can be computed, sum
each level to get the total water capacity.
"""

class Solution:
    def trap(self, height) -> int:
        n = len(height)
        if n <= 2: return 0
        dp = [1]*n
        l,r = 0,n-1
        t = n
        d = {}
        for i in range(n):
            if d.get(height[i]) == None: d[height[i]] = list()
            d[height[i]].append(i)
        ans = 0

        for j in range(100002):
            # delete points
            if d.get(j) != None:
                for k in d[j]:
                    t -= 1
                    dp[k] = 0
            if t <= 1: return ans
            # correct range points
            while dp[l] == 0:
                l += 1
            while dp[r] == 0:
                r -= 1
            ans += (r-l+1-t)
        return ans