class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # if len(nums)<2:
        #     return 
        left=0
        right=len(nums)-1

        while left<right:
            mid=(left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left+=1
            else:
                right-=1

        if nums[left]<target:
            return left+1
        if nums[left]>=target:
            return left
        