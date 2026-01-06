"""
O(n log n) would be trivial, so we need to get a bit creative here
store values in a dict, and then this is a "connected component" search
checked dict is to ensure each unique value is only accessed at most once

Runtime: O(n)
"""

class Solution:
    def longestConsecutive(self, nums) -> int:
        d = {}
        for i in nums:
            d[i] = 1
        checked = {}
        ans = 0
        for j in d.keys():
            if checked.get(j) == None: # compute length of this segment
                checked[j] = 1
                a,b = j,j
                while d.get(a-1) != None:
                    a -= 1
                    checked[a] = 1
                while d.get(b+1) != None:
                    b += 1
                    checked[b] = 1
                ans = max(ans,b-a+1)
        return ans