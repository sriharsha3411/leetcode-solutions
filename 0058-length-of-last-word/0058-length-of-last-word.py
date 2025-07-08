class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count=1
        char_count=0
        for i in range(len(s)-1,-1,-1):

            if char_count==1 and s[i]==" ":
                break
                
            if s[i].isalpha() and char_count==0:
                char_count+=1
                continue

            if s[i].isalpha() and char_count==1:
                count+=1

            

        return count

