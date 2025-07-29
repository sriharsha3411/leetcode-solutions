class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        negative_count=0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    negative_count += 1
                
        return negative_count