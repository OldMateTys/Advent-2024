class Solution:

    map = []
    visited = []

    def __init__(self, map):
        self.map = map

        for i in range(len(map)):
            new_row = []
            for j in range(len(map[0])):
                new_row.append(False)
            self.visited.append(new_row)
        
        trails = 0
        for i in range(len(map)):
            for j in range(len(map[0])):
                new_count = self.dfs(i, j, -1, '')
                trails += new_count
                self.reset_visited()
    
    def reset_visited(self):
        for i in range(len(self.visited)):
            for j in range(len(self.visited[0])):
                self.visited[i][j] = False
        

    
    def dfs(self, i, j, prev, direction) -> int:
        
        if i < 0 or i > len(self.map) - 1:
            return 0
        if j < 0 or j > len(self.map[0]) - 1:
            return 0
        
        num = int(self.map[i][j])
        
        if num != prev + 1:
            return 0
        
        if num == 9:
            return 1
        
        path_count = 0
        
        path_count += self.dfs(i+1, j  , num, 'down')
        path_count += self.dfs(i-1, j  , num, 'up')
        path_count += self.dfs(i  , j-1, num, 'left')
        path_count += self.dfs(i  , j+1, num, 'right')

        return path_count
        
        
        
def main():

    map = []

    with open('trails.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_ls = []
            for char in line:
                if char.isspace():
                    continue
                line_ls.append(char)
            
            map.append(line_ls)
    print(map)
    s = Solution(map)



if __name__ == "__main__":
    main()