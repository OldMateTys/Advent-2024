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

        
    def printLines(self):
        print()
        print(f"Direction: {self.dir}")
        print(f"Loopchecker: {self.loopCheck}")

        for line in self.route:
            string = ""
            for char in line:
                string += char
            print(string)

    def checkLoop(self):
        x, y = self.x, self.y
        i, j = self.o
        
        match self.dir:
            case 0:
                if y == i + 1 and x == j:
                    self.loopCheck[0] += 1
                    if self.loopCheck[0] == 2:
                        return True
            case 1:
                if y == i and x == j - 1:
                    self.loopCheck[1] += 1
                    if self.loopCheck[1] == 2:
                        return True
            case 2:
                if y == i - 1 and x == j:
                    self.loopCheck[2] += 1
                    if self.loopCheck[2] == 2:
                        return True
            case 3:
                if y == i and x == j + 1:
                    self.loopCheck[3] += 1
                    if self.loopCheck[3] == 2:
                        return True
            
        return False

    def run(self):
        loop = 0
        while True:
            
            if self.checkLoop():
                return True
            self.route[self.y][self.x] = "X"
            prev_x, prev_y = self.x, self.y
            icon = self.moveCursor()
            
            if self.atEdgeOfBoard():
                break
            self.route[self.y][self.x] = icon
            
            if (self.x, self.y) in self.been:
                if self.dir in self.been[(self.x, self.y)]:
                    # print(self.x)
                    # print(self.y)
                    # print('this')
                    return True
                else:
                    self.been[(self.x, self.y)].append(self.dir)
            else:
                self.been[(self.x, self.y)] = [(self.dir)]
            # print(self.been)
            i, j = self.o


            if icon == "X":
                break
        
        return False
    def obstructionCalc(self):
        total_count = len(self.route) * len(self.route[0])
        start_x = self.x
        start_y = self.y
        obsCount = 0
        for i, row in enumerate(self.route):
            for j, item in enumerate(row):
                if i == start_y and j == start_x:
                    continue
                if item == "#":
                    continue
                self.o = i, j
                self.route[i][j] = "O"
                self.been = {}
                
                if self.run():
                    obsCount += 1
                    #self.printLines()

                self.dir = 0
                self.x, self.y = start_x, start_y
                self.loopCheck = [0, 0, 0, 0]
                self.route[i][j] = "."
                self.route[start_y][start_x] = "^"
                
                print(f"Progress: {j + len(self.route[0] * i)} / {total_count}")
                

                
        print(obsCount)

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
    print(route)

    s = Solution(route, x, y, dir)
    s.obstructionCalc()


if __name__ == "__main__":
    main()