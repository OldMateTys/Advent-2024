from collections import deque
import time

class Robot:

    def __init__(self, x, y, px, py):
        self.x  = x
        self.y  = y
        self.px = px
        self.py = py

    def move(self, count, width, length):
        self.px = (self.px + count * self.x) % width
        self.py = (self.py + count * self.y) % length

def run():
    pass
def main():

    width, length = 101, 103
    robots = deque()
    with open('robots.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            line_ls = line.strip().split()
            position = line_ls[0][2:].split(",")
            px = int(position[0])
            py = int(position[1])
            
            velocity = line_ls[1][2:].split(",")
            x = int(velocity[0])
            y = int(velocity[1])

            robot = Robot(x, y, px, py)
            robots.append(robot)
    

    
    map = []
    for i in range(length):
        map_ls = []
        for j in range(width):
            map_ls.append('.')
        map.append(map_ls)
    print(len(robots))
    count = 68
    for robot in robots:
        robot.move(7037, width, length)
    
    while True:
        for i in range(len(map)):
            for j in range(len(map[0])):
                map[i][j] = "."
        
        for robot in robots:
            robot.move(101, width, length)
            if map[robot.py][robot.px] != '.':
                map[robot.py][robot.px] = str(int(map[robot.py][robot.px]) + 1)
            else:
                map[robot.py][robot.px] = '1'
        count += 101
        print()
        for row in map:
            string = ""
            for col in row:
                string += col
            print(string)
        print(f"Iteration: {count}")

        time.sleep(0.2)
        
    halfWidth = width // 2
    print(halfWidth)
    halfLength = length // 2

    q1_count = 0
    for i in range(halfLength):
        for j in range(halfWidth):
            if map[i][j] != '.':
                q1_count += int(map[i][j])
    q2_count = 0
    for i in range(halfLength + 1, length):
        for j in range(halfWidth + 1, width):
            if map[i][j] != '.':
                q2_count += int(map[i][j])
    q3_count = 0
    for i in range(halfLength):
        for j in range(halfWidth + 1, width):
            if map[i][j] != '.':
                q3_count += int(map[i][j])
    q4_count = 0
    for i in range(halfLength + 1, length):
        for j in range(halfWidth):
            if map[i][j] != '.':
                q4_count += int(map[i][j])
    
    total = q1_count * q2_count * q3_count * q4_count
    print(total)

if __name__ == "__main__":
    main()