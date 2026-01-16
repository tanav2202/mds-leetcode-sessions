class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        missing = len(t)

        best_len = float("inf")
        best_l = 0

        l = 0
        for r , ch in enumerate(s):
            if need[ch] > 0:
                missing-=1
            
            need[ch]-=1
            while missing == 0:
                window_len = r - l + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = l
                left_ch = s[l]
                need[left_ch] +=1

                if need[left_ch] > 0:
                    missing+=1
                l+=1
        if best_len == float("inf"):
            return ""
        best_len = int(best_len)

        return s[best_l: best_l + best_len]
