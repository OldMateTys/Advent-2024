import math
from collections import deque

class Solution():

    data = []

    def __init__(self, data):
        self.data = data

    def run(self):
        
        total_tokens = 0
        
        for i, item in enumerate(self.data):
            a_x, a_y = item['A']
            b_x, b_y = item['B']
            p_x, p_y = item['P']
            

            num_b = (p_y*a_x - p_x * a_y) / (b_y *a_x - b_x * a_y)
            num_a = num_b * (p_x * b_y - p_y * b_x) / (a_x * p_y - p_x * a_y)
            
            
            
            print(f"A Count: {num_a} | B Count: {num_b}")
            print(f"Comparing: SumX={num_b*b_x + num_a*a_x} | {p_x}")
            print(f"Comparing: SumY={num_b*b_y + num_a*a_y} | {p_y}")
            
            if ((0 <= num_b - int(num_b) < 1e-3 or 0 <= int(num_b) - num_b + 1 < 1e-3) and 
                (0 <= num_a - int(num_a) < 1e-3 or 0 <= int(num_a) - num_a + 1 < 1e-3)):
                print("adding")
                total_tokens += 3 * num_a + num_b

            
            print()

        print(total_tokens)
        print()


            




def main():
    print('data')
    data = deque()
    with open('text.txt', 'r') as file:
        
        lines = file.readlines()
        i = 0
        while i < len(lines):
            try:
                
                a = lines[i].strip().split(" ")
                i+=1
                b = lines[i].strip().split(" ")
                i+=1
                prize = lines[i].strip().split(" ")
                i+=2

                a_x = int(a[1+1][2:][:-1])
                a_y = int(a[2+1][2:])

                b_x = int(b[1+1][2:][:-1])
                b_y = int(b[2+1][2:])

                prize_x = int(prize[1][2:][:-1]) + 10000000000000
                prize_y = int(prize[2][2:]) + 10000000000000




                data_dict = {'A': (a_x, a_y), 'B': (b_x, b_y), 'P':(prize_x, prize_y)}
                data.append(data_dict)

                
            except:
                print("failed. exitting.")
                exit(1)
    print(data)

    s = Solution(data)
    s.run()

if __name__ == "__main__":
    main()
