class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        # for i in range(k):
        #     temp = nums[l-1]
        #     nums.insert(0,temp)
        #     nums.pop()
        k=k%l
        def reverse(i,j,arr):
            while i<j:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                i+=1
                j-=1

        reverse(0,l-1,nums)
        reverse(0,k-1,nums)
        reverse(k,l-1,nums)




        
            