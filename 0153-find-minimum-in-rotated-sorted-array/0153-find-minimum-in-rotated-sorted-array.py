class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left=0
        right=len(nums)-1
        minn=float('inf')
        

        while left<=right:

            mid=(left+right)//2

            if nums[left]<=nums[mid]:
                if nums[left]<=minn:
                    minn=nums[left]
            

                left=mid+1

            else:
                if nums[mid]<=minn:
                    minn=nums[mid]
                right=mid-1
            
        return minn
                