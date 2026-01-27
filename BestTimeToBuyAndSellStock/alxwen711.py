class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        mv = 10001 # maximum is 10000
        for p in prices:
            ans = max(ans,p-mv)
            mv = min(mv,p)
        return ans
        