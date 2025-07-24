class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # return -1

        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            

            if nums[mid]==target:
                return mid

            elif nums[left]<=nums[mid]:
                if target>=nums[left] and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1



            # elif nums[mid]>target:
            
            #     if target<nums[left]:
            #         left=mid+1
            #     else:
            #         right=mid-1
            # else:
            #     if target>nums[right]:
            #         right=mid-1
            #     else:
            #         left=mid+1
        return -1
            
                

