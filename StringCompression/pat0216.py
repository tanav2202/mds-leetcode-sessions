class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 # iterator
        index = 0 #iterator for output list
        while i < len(chars):
            current_char = chars[i]
            count = 0
         
            while i < len(chars) and chars[i] == current_char:
                count +=1
                i += 1
            chars[index] = current_char
            index += 1

            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1
        return index
        
            
