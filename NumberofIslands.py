class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_num = len(grid)
        if row_num == 0:
            return 0
        col_num = len(grid[0])

        count = 0
        start_r, start_c = self.find_index(grid, row_num, col_num)
        while (start_r, start_c) != (-1,-1):
            count += 1
            stack = []
            stack.append((start_r, start_c))
            print (start_r, start_c)
            while not stack == []:
                (i, j) = stack.pop()      
                grid[i][j] = '0'
                if i > 0:
                    if grid[i-1][j] == '1':
                        stack.append((i-1,j))
                if i < row_num - 1:
                    if grid[i+1][j] == '1':
                        stack.append((i+1,j))
                if j > 0:
                    if grid[i][j - 1] == '1':
                        stack.append((i,j-1))
                if j < col_num - 1:
                    if grid[i][j + 1] == '1':
                        stack.append((i,j+1))
            start_r, start_c = self.find_index(grid, row_num, col_num)
        return count
    def find_index(self, grid, n , k):
        for i in range(n):
            for j in range(k):
                if grid[i][j] == '1':
                    return (i,j)
        return (-1,-1)
