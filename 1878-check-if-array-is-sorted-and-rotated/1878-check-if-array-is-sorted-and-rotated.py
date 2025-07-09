class Solution:
    def check(self, nums: List[int]) -> bool:
    
        count=0
        l=len(nums)
        for i  in range(0,l):
            if nums[i]>nums[(i+1)%l]:
                count+=1
        
        if count>1:
            return False
        else:
            return True


        

            