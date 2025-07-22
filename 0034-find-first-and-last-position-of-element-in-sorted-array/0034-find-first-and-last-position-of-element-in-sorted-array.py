class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        first_occurence=-1
        last_occurence=-1
    
        
        while left<=right:
            mid=(left+right)//2
            
            if nums[mid]==target:
                first_occurence=mid
                right=mid-1    #to find fisrt occurence of target
            
            elif target>nums[mid]:
                left=mid+1
            
            else:
                right=mid-1

        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            
            if nums[mid]==target:
                last_occurence=mid
                left=mid+1     #to find last occurence of target
            
            elif target>nums[mid]:
                left=mid+1
            
            else:
                right=mid-1
        
        return [first_occurence,last_occurence]