from collections import deque
import math

class Solution:
    
    def __init__(self, route, x, y, dir):
        self.route = route
        self.x, self.y = x, y
        self.dir = dir
        self.starting_route = route.copy()
        self.loopCheck = [0, 0, 0, 0]
        self.o = 0, 0
        self.been = {}

    def atEdgeOfBoard(self):
        if self.x < 0  or self.x > len(self.route[0]) - 1:
            return True
        if self.y < 0  or self.y > len(self.route) - 1:
            return True
        return False
    
    
    def moveCursor(self):
        match self.dir:
            case 0:
                if self.y > 0:
                    if self.route[self.y - 1][self.x] in ("#", "O"):
                        self.dir += 1
                        return self.moveCursor()
                self.y -= 1
                return "^"
            case 1:
                if self.x < len(self.route[0]) - 1:
                    if self.route[self.y][self.x + 1] in ("#", "O"):
                        self.dir += 1
                        
                        return self.moveCursor()
                self.x += 1
                return ">"
            case 2:
                if self.y < len(self.route) - 1:
                    if self.route[self.y + 1][self.x] in ("#", "O"):
                        self.dir += 1
                        return self.moveCursor()
                self.y += 1
                return "v"
            case 3:
                if self.x > 0:
                    if self.route[self.y][self.x - 1] in ("#", "O"):
                        self.dir = 0
                        return self.moveCursor()
                self.x -= 1
                return "<"


    def run(self):

        while True:
            
            self.route[self.y][self.x] = "X"
            icon = self.moveCursor()
            
            if self.atEdgeOfBoard():
                break
            self.route[self.y][self.x] = icon
            
            if (self.x, self.y) in self.been:
                if self.dir in self.been[(self.x, self.y)]:
                    return True
                else:
                    self.been[(self.x, self.y)].append(self.dir)
            else:
                self.been[(self.x, self.y)] = [(self.dir)]


            if icon == "X":
                break
        self.printBoard()
        return False

    def printBoard(self):
        for line in self.route:
            string = ""
            for char in line:
                string += char
            print(string)
                

def main():
    route = deque()
    y: int
    x: int
    dir:int
    with open('route.txt', 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            ls = []
            line = line.strip()
            for j, char in enumerate(line):
                ls.append(char)
                if char in ("^", ">", "<", "v"):
                    y = i
                    x = j
                    match char:
                        case "^":
                            dir = 0
                        case ">":
                            dir = 1
                        case "v":
                            dir = 2
                        case "<":
                            dir = 3                                                      
            route.append(ls)
    s = Solution(route, x, y, dir)
    s.run()

if __name__ == "__main__":
    main()