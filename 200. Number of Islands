200. Number of Islands
This is a dsf solution to a very commonly asked amazon problem:https://leetcode.com/problems/number-of-islands/submissions/

class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        x=0;
        #scan every element looking for a 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1'):
                    x+=1;
                    holder = bfs(grid,i,j)
                    
                        
        return x
        #once a 1 is found start a bfs searching until every connected element is turned into a 0
        #once bfs is compelte it returns true?
        #count number of true returns.
def bfs(grid,i,j):
    
    #look up
    if(i not in range(len(grid)) or j not in range(len(grid[0]))):
        return True;     
    print(i)
    print(j)
    if(grid[i][j]=='0'):
        return True
    grid[i][j]='0'
    bfs(grid,i-1,j)
    #look down
    
    bfs(grid,i+1,j)
    #look left

    
    bfs(grid,i,j+1)
    #look right

    bfs(grid,i,j-1)
