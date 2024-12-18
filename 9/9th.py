from collections import deque

class Solution():
    line = []

    def __init__(self, line):
        self.line = line

    def printLine(self):
        new_line = []
        for item in self.line:
            for i in range(item[1]):
                new_line.append(item[0])
        print(new_line)

    def iterate(self):
        
        i = len(self.line) - 1
        while i >= 0:

            curr_id = self.line[i][0]
            curr_num = self.line[i][1]
            if curr_id == -1:
                i -= 1
                continue
            j = 0   
            while j < i:
                left_id, left_num = self.line[j]
                if left_id != -1:
                    j += 1
                    continue
                if left_num < curr_num:
                    j += 1
                    continue
                
                remaining_space = left_num - curr_num
                self.line[j] = (curr_id, curr_num)
                self.line[i] = (-1, curr_num)
                if remaining_space != 0:
                    self.line.insert(j+1, (-1, remaining_space))
                    i+=1

                break


            i -= 1


    def count(self):
        count = 0
        new_line = []
        for item in self.line:
            for i in range(item[1]):
                new_line.append(item[0])
        for i, num in enumerate(new_line):
            if num < 0:
                continue
            count += i * num

        print(f"Count: {count}")


def main():
    array = deque()
    
    with open('files.txt', 'r') as file:

        lines = file.readlines()
        array = lines[0].strip()
    
    blocks = deque()
    space  = deque()
    line = []
    curr_id = 0

    for i in range(len(array)):
        num = int(array[i])
        if i % 2 == 0:
            
            line.append((curr_id, num))
            curr_id += 1
        else:
            
            line.append((-1, num))

    s = Solution(line)
    s.iterate()
    s.count()


if __name__ == "__main__":
    main()