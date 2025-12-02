class Solution:
    def compress(self, chars) -> int:
        pi = 0
        prev = chars[0]
        ansp = 0
        for i in range(len(chars)):
            if prev != chars[i]: # write in answer
                count = i-pi
                chars[ansp] = prev
                ansp += 1
                if count != 1:
                    s = str(count)
                    for j in s:
                        chars[ansp] = j
                        ansp += 1
                pi = i
                prev = chars[i]
        # complete last group
        count = len(chars)-pi
        chars[ansp] = prev
        ansp += 1
        if count != 1:
            s = str(count)
            for j in s:
                chars[ansp] = j
                ansp += 1
        return ansp