import math
from collections import deque
import time

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def checkAhead(self, map, x, y, direction):

        if map[y][x] == "#":
            return False
        if map[y][x] == ".":
            return True
        
        match direction:
            case 0:
                return self.checkAhead(map, x, y-1, direction)
            case 1:
                return self.checkAhead(map, x+1, y, direction)
            case 2:
                return self.checkAhead(map, x, y+1, direction)
            case 3:
                return self.checkAhead(map, x-1, y, direction) 
            
    def setAhead(self, map, x, y, direction):                                        

        if map[y][x] == ".":
            map[y][x] = "O"
            return 

        match direction:
            case 0:
                return self.setAhead(map, x, y-1, direction)
            case 1:
                return self.setAhead(map, x+1, y, direction)
            case 2:
                return self.setAhead(map, x, y+1, direction)
            case 3:
                return self.setAhead(map, x-1, y, direction) 
        
    def move(self, map, direction):
        map[self.y][self.x] = "."
        match direction:
            case 0:
                self.y -= 1
                
            case 1:
                self.x += 1
            case 2:
                self.y += 1
            case 3:
                self.x -= 1
        map[self.y][self.x] = "@"
        

def run1(robot, map, instructions):

    for i, item in enumerate(instructions):
        
        direction = ""

        match item:
            case "^":
                direction = 0
            case ">":
                direction = 1
            case "v":
                direction = 2
            case "<":
                direction = 3

        if robot.checkAhead(map, robot.x, robot.y, direction):

            robot.setAhead(map, robot.x, robot.y, direction)
            robot.move(map, direction)

    total = 0
    for i, line in enumerate(map):
        #print(line)
        for j, char in enumerate(line):
            total += 100*i + j if char == "O" else 0
    #print()
    #print(total)   

def run2(robot, map, instructions):
    pass



def main():
    
    map = []
    instructions = deque()
    with open('submarine.txt', 'r') as file:
        lines = file.readlines()
        isMap = True
        x, y = 0, 0
        for i, line in enumerate(lines):
            if line.isspace():
                isMap = False
                continue
                
            mapls = deque()
            for j, char in enumerate(line.strip()):
                
                if isMap:
                    mapls.append(char)
                    if char == "@":
                      x, y, = j, i  
                else:
                    instructions.append(char)
            if mapls:
                map.append(mapls)

    

    robot = Robot(x, y)
    run(robot, map, instructions)


if __name__ == "__main__":
    main()