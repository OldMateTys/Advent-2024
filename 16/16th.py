import math
from collections import deque
import random
import heapq
import itertools

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = []
        self.visited = False
        self.distance = float('inf')
        self.letter = ""
        self.parent = None
        self.dir = None
        self.path = None
        self.child = None
    
    def addNeighbour(self, node: 'Node'):
        self.neighbours.append(node)
    
    def setDistance(self, distance):
        self.distance = distance
    
    def getNeighbours(self):
        return self.neighbours
    

class Reindeer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.memo = {}
        self.shortest_path = float('inf')
        self.loop = 0
        

    def move(self, direction, forwards=True):
        match direction:
            case 0:
                self.y -= 1 if forwards else -1
            case 1:
                self.x += 1 if forwards else -1
            case 2:
                self.y += 1 if forwards else -1
            case 3:
                self.x -= 1 if forwards else -1


def getWeight(direction, node1: Node, node2: Node):

    if (direction == 0 and node2.y < node1.y or
        direction == 1 and node2.x > node1.x or
        direction == 2 and node2.y > node1.y or 
        direction == 3 and node2.x < node1.x):
        return 1
    return 1001

def getDirection(node1, node2):
    if node2.y < node1.y:
        return 0
    if node2.x > node1.x:
        return 1
    if node2.y > node1.y:
        return 2
    if node2.x < node1.x:
        return 3
    
def dijkstras(map, start: Node, end: Node):

    queue = [(0, 0, 1, start)]
    heapq.heapify(queue)
    print(queue)
    c = itertools.count(1, 1)

    dir = 1
    while True:

        
        dist, count, dir, currentNode = heapq.heappop(queue)

        parent = currentNode.parent
        if parent is not None:
            parent.child = currentNode
        
        prev = currentNode.letter
        currentNode.letter = "A"
        currentNode.letter = prev
        x, y = currentNode.x, currentNode.y

        currentNode.letter = "X"

        if currentNode is end:

            return dist
        
        if currentNode.visited:
            continue

        currentNode.visited = True
        currentNode: Node
        for node in currentNode.getNeighbours():

            if node.visited:
                continue
            direction = getDirection(currentNode, node)
            node: Node
            weight = getWeight(dir, currentNode, node)
            if dist + weight < node.distance:
                node.distance = dist + weight
                node.parent = currentNode
                node.dir = direction

            heapq.heappush(queue, (node.distance, next(c), direction, node))

        prev = currentNode

    


def printBoard(map, start, end):
    for line in map:
        string = ""
        for char in line: 
            if char is None:
                string += "."
                continue
            if char.letter == "X":
                string += "X"
                continue
            if char.letter == "A":
                string += "A"
                continue
            if char.letter == "O":
                string += "O"
                continue
            if char is start:
                string += "S"
                continue
            if char is end:
                string += "E"
                continue
            if isinstance(char, Node):
                string += "."
                continue
        print(string)
    print()


def run(map, nodeList, start: Node, end: Node):

    dist = dijkstras(map, start, end)
    print(dist)
    current = end
    current: Node
    path = deque()
    for line in map:
        for node in line:
            if node is None:
                continue
                
            node: Node
            current = node
            path = deque()
            while current is not None:
                path.appendleft(current)
                current = current.parent
            node.path = path

    
    path_elements = set(end.path)
    print(len(path_elements))
    prev = None
    iter = set(path_elements)
    for node in nodeList:
        node.letter = "."
    start.letter = "S"
    end.letter = "E"
    for node in path_elements:
        node.letter = "O"
        #print(node.letter)
    printBoard(map, start, end)
    count = 0
    while len(iter) > 0:
        newSet = set()
        for node in iter:
            for n in node.getNeighbours():

                if n in path_elements:
                    continue

                n: Node
                
                if node == end:
                    continue                

                if node.child is None:
                    
                    dist = n.distance + getWeight(n.dir, n, node)
                    if dist == node.distance:

                        path_elements.update(set(n.path))
                        newSet.update(set(n.path))
                else:


                    distBetween = n.distance + getWeight(n.dir, n, node) + getWeight(getDirection(n, node), node, node.child)
                    
                    if  distBetween == node.child.distance:
                        for node in nodeList:
                            node.letter = "."
                        start.letter = "S"
                        end.letter = "E"
                        for node in path_elements:
                            node.letter = "O"

                        path_elements.update(set(n.path))
                        newSet.update(set(n.path))
                

        iter = newSet
        for thing in nodeList:
            thing.letter = "."
        start.letter = "S"
        end.letter = "E"
        for thing in path_elements:
            thing.letter = "O"
            #print(node.letter)
        printBoard(map, start, end)
                

    print(len(path_elements))
    # print(len(path_elements))
    for node in nodeList:
        node.letter = "."
    start.letter = "S"
    end.letter = "E"
    for node in path_elements:
        node.letter = "O"
        #print(node.letter)
    printBoard(map, start, end)






def main():
    
    map = []
    nodeList = []
    start = None
    end = None

    with open('reindeer.txt', 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            line = line.strip()
            ls2 = []

            for j, char in enumerate(line):
                
                new_node = Node(j, i)
                if char != "#":
                    ls2.append(new_node)
                    nodeList.append(new_node)
                    new_node.letter = "."
                
                    if char == "S":
                        start = new_node
                        start.letter = "S"
                    if char == "E":
                        end = new_node
                        end.letter = "E"
                else:
                    ls2.append(None)
            map.append(ls2)

    printBoard(map, start, end)
    for i, line in enumerate(map):
        for j, spot in enumerate(line):
            if not isinstance(spot, Node):
                continue
            node = spot
            if i > 0:
                if map[i-1][j] is not None:
                    node.addNeighbour(map[i-1][j])
            if i < len(map) - 1:
                if map[i+1][j] is not None:
                    node.addNeighbour(map[i+1][j])
            if j > 0:
                if map[i][j-1] is not None:
                    node.addNeighbour(map[i][j-1])
            if j < len(map[0]) - 1:
                if map[i][j+1] is not None:
                    node.addNeighbour(map[i][j+1])
    start.setDistance(0)
    run(map, nodeList, start, end)

if __name__ == "__main__":
    main()