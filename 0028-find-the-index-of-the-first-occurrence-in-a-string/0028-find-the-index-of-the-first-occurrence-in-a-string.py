class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack) ==1 :
            if needle == haystack :
                return 0
            else:
                return -1
        i=0
        j=len(needle)

        while j<=len(haystack):
            if haystack[i:j] == needle:
                return i
            else:
                i+=1
                j+=1

        return -1

       


