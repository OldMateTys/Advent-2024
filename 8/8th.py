import math

class Solution:
    
    map = []
    node = []

    def __init__(self, map, node):
        self.map = map
        self.node = node

    def recur(self, i, j, i_incremenet, j_increment, letter):
        # print(f"- Location: ({j}, {i}) | Letter: {letter}")
        
        if i < 0 or i >= len(self.map):
            return
        if j < 0 or j >= len(self.map[0]):
            return

        self.node[i][j] = True


        self.recur(i+i_incremenet, j+j_increment, i_incremenet, j_increment, letter)

    def checkBoundaries(self, x, y):
        if x < 0 or x >= len(self.map[0]):
            return False
        if y < 0 or y >= len(self.map):
            return False
        return True
    
    def compute(self):
        antennas = {}

        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                letter = self.map[i][j]
                if letter == '.':
                    continue
                self.node[i][j] = "#"
                if letter in antennas:
                    antennas[letter].append((i, j))
                else:
                    antennas[letter] = [(i, j)]
        # print('here')
        for item in antennas:
            # print(item)
            # print(antennas)
            for i in range(len(antennas[item])):
                for j in range(len(antennas[item])):
                    # print(item)
                    # print(antennas[item])

                    location_1 = antennas[item][i]
                    location_2 = antennas[item][j]
                    if location_1 == location_2:
                        continue
                    
                    x_1 = location_1[1]
                    x_2 = location_2[1]
                    y_1 = location_1[0]
                    y_2 = location_2[0]

                    x_dist = abs(x_1 - x_2)
                    y_dist = abs(y_1 - y_2)

                    x_right = max(x_1, x_2)
                    x_left = min(x_1, x_2)

                    y_bot = max(y_1, y_2)
                    y_top = min(y_1, y_2)

                    letter = item
                    # print(antennas[item])
                    print(f"i: {i} | j: {j} | item: {item}")
                    if (x_1 > x_2 and y_1 > y_2) or (x_2 > x_1 and y_2 > y_1):

                        # print(f"Recurring: ({x_left, y_top}) | Up-Left | Letter: {letter}")
                        self.recur(y_top - y_dist, x_left - x_dist, -y_dist, -x_dist, letter)

                        self.node[y_bot][x_right] = True if self.checkBoundaries(y_top - y_dist, x_left - x_dist) else self.node[y_bot][x_right]
                        self.node[y_top][x_left] = True if self.checkBoundaries(y_top - 2*y_dist, x_left - 2*x_dist) else self.node[y_top][x_left]
                        
                        
                        # print(f"Recurring: ({x_right, y_bot} | Down-Right) | Letter: {letter}")
                        self.recur(y_bot + y_dist, x_right + x_dist, y_dist, x_dist, letter)  

                        self.node[y_top][x_left]  = True if self.checkBoundaries(y_bot + y_dist, x_right + x_dist) else self.node[y_top][x_left]
                        self.node[y_bot][x_right] = True if self.checkBoundaries(y_bot + 2*y_dist, x_right + 2*x_dist) else self.node[y_bot][x_right]

                    else:
                        # print(f"Recurring: ({x_right, y_top}) | Up-Right | Letter: {letter}")

                        self.recur(y_top - y_dist, x_right + x_dist, -y_dist, x_dist, letter)

                        self.node[y_bot][x_left] = True if self.checkBoundaries(y_top - y_dist, x_right + x_dist) else self.node[y_top][x_right]
                        self.node[y_top][x_right] = True if self.checkBoundaries(y_top - 2*y_dist, x_right + 2*x_dist) else self.node[y_top][x_right]


                        # print(f"Recurring: ({x_left, y_bot}) | Down-left | Letter: {letter}")
                        self.recur(y_bot + y_dist, x_left - x_dist, y_dist, -x_dist, letter)
                        self.node[y_top][x_right] = True if self.checkBoundaries(y_bot + y_dist, x_left - x_dist) else self.node[y_top][x_right]
                        self.node[y_bot][x_left] = True if self.checkBoundaries(y_bot + 2 * y_dist, x_left - 2 *x_dist) else self.node[y_bot][x_left]

        
        count = 0
        for i, line in enumerate(self.node):
            
            for j, nodule in enumerate(line):

                if nodule:
                    if self.map[i][j] == '.':
                        self.map[i][j] = '#'
                    count += 1
        
        for line in self.node:
            string = ''
            for letter in line:
                
                string += "#" if letter else "."
            print(string)
        
        print(count)

def main():
    
    map = []
    node = []
    with open('antennas.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            ls = []
            ls2 = []
            for item in line:
                if item.isspace():
                    continue
                ls.append(item)
                ls2.append(False)
            map.append(ls)
            node.append(ls2)
    
    s = Solution(map, node)
    s.compute()

if __name__ == "__main__":
    main()