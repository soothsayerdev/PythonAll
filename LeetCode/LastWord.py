class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sInvert = s[::-1].strip()
        lastWord = ""
 
        for i in sInvert:
            if i != " ":
                lastWord += i
            else:
                break

        
        
        return len(lastWord)
    

test = "  i fly  to the moon  "
obj = Solution()
print(obj.lengthOfLastWord(test))
