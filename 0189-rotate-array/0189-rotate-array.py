class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        for i in range(k):
            temp = nums[l-1]
            nums.insert(0,temp)
            nums.pop()
        
            