class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        
        sorted_d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))

        count=0
        l=[]
        for i in sorted_d.keys():
            l.append(i)
            count+=1
            if count==k:
                break
        
        return l

        