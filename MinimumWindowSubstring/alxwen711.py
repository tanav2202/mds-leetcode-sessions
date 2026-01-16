class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # create frequency count of string t
        h = [0]*128
        p = 0 # unique chr count in t
        for i in t:
            x = ord(i)
            if h[x] == 0: p += 1
            h[x] += 1
        
        # slide rightpt until fully contained
        n = len(s)
        lp,rp = 0,-1
        for j in range(n):
            y = ord(s[j])
            h[y] -= 1
            if h[y] == 0: p -= 1 # all instances of specific type of char in t have been fufilled
            if p == 0: # found shortest (all chars in t have been found)
                rp = j
                break
        if rp == -1: return "" # no solution found

        # run two pointer from here
        bestlen = rp # minimize rp - lp
        bestindex = 0
        
        # try pushing lp first before attempting to push rp
        while lp <= rp:
            pt = ord(s[lp])
            if h[pt] == 0: break # cannot push further
            h[pt] += 1
            lp += 1
        if rp-lp < bestlen: # replace best answer
            bestlen = rp-lp
            bestindex = lp
        
        # now try pushing rp
        for l in range(rp+1,n):
            h[ord(s[l])] -= 1
            while lp <= l:
                pt = ord(s[lp])
                if h[pt] == 0: break # cannot push further
                h[pt] += 1
                lp += 1
            if l-lp < bestlen: # replace best answer
                bestlen = l-lp
                bestindex = lp
        return s[bestindex:bestindex+bestlen+1]