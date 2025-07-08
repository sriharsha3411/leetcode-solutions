class Solution:
    def secondHighest(self, s: str) -> int:
        max=-1
        second_max=-1

        for i in range(len(s)):
            if s[i].isdigit():
                if int(s[i])>max:
                    second_max=max
                    max=int(s[i])

                if int(s[i])>second_max and int(s[i])<max:
                    second_max=int(s[i])
        return second_max