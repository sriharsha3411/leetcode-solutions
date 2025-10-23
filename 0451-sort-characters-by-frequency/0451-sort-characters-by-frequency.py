class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for char in s:
            d[char]=d.get(char,0)+1

        sorted_d = dict(sorted(d.items(), key = lambda x:x[1],reverse=True))

        result=""
        for key,value in sorted_d.items():
            result += (key*value)
        
        return result
            