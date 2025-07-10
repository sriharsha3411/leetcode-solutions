class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        maxx=1

        i=0

        for j in range(1,len(s)):
            if s[i]==s[j]:
                count+=1
                maxx=max(maxx,count)
            else:
                i=j
                count=1
        return maxx
