class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        negative_count=0

        for i in range(len(grid)):
            # for j in range(len(grid[i])):
            #     if grid[i][j] < 0:
            #         negative_count += 1


            left=0
            right=len(grid[i])-1

            while left<=right:
                mid=(left+right)//2

                if grid[i][mid]<0:
                    negative_count += right-mid+1
                    right = mid-1
                else:
                    left = mid+1
                
        return negative_count