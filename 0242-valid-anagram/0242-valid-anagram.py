class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if len(s)==len(t):
        #     if sorted(s)==sorted(t):
        #         return True
        #     else:
        #         return False

        # return False

        s_hashmap={}
        for char in s:
            s_hashmap[char]=s_hashmap.get(char,0)+1
        t_hashmap={}
        for char in t:
            t_hashmap[char]=t_hashmap.get(char,0)+1
        
        if s_hashmap==t_hashmap:
            return True
        else:
            return False
        
