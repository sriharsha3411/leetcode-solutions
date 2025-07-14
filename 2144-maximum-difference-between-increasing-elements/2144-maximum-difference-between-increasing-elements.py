class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx=-1
        minn=nums[0]
        
        for i in range(1,len(nums)):
            if nums[i]-minn > maxx:
                maxx=nums[i]-minn
            minn=min(minn,nums[i])

        if maxx==0:
            return -1
        return maxx
