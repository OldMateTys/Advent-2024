import math
from collections import deque

class Robot:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def checkAhead():
        pass

    
def run():
    pass
def main():
    
    map = []
    instructions = deque()

    with open('submarine.txt', 'r') as file:
        lines = file.readlines()
        isMap = True
        for line in lines:
            if line.isspace():
                isMap = False
                continue
                
            mapls = deque()
            for char in line.strip():

                if isMap:
                    mapls.append(char)
                else:
                    instructions.append(char)
            if mapls:
                map.append(mapls)

    print(map)
    print(instructions)


if __name__ == "__main__":
    main()