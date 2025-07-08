class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        rev_s=""
        for char in s:
            if char.isalnum():
                new_s+=char.lower()
                rev_s=char.lower()+rev_s
        
        

        if new_s == rev_s:
            return True
        else:
            return False

