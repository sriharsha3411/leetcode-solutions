class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        

        for i in range(len(nums)):
            if len(nums)==1:
                return 0
            if i==0 and nums[i]>nums[i+1]:
                return 0

            elif i==len(nums)-1 and nums[i]>nums[i-1]:
                return len(nums)-1

            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
            else:
                continue
        
            