class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left=0
        new_s=set()
        count=0

        for right in range(len(s)):
            while s[right] in new_s:
                new_s.remove(s[left])
                left+=1
            count=max(count,right-left+1)
            new_s.add(s[right])


        return count
