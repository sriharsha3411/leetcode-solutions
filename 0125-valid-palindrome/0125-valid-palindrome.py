class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s=""
        for i in s:
            if i.isalnum():
                new_s+=i.lower()
        
        i=0
        j=len(new_s)-1
        count=0
        while(i<j):
            if new_s[i] != new_s[j]:
                count+=1

            i+=1
            j-=1
        
        if count==0:
            return True
        else:
            return False







