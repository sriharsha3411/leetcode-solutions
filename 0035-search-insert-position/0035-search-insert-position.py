class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1
        ans=-1

        while left<=right:
            mid=(left+right)//2

            if nums[mid]>=target:
                ans=mid
                right=mid-1
            else:
                left=mid+1

        if ans==-1:
            return len(nums)
        else:
            return ans





            
        