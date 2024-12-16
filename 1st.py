import math
from collections import deque

def run():
    pass

def main():
    
    numsL = deque()
    numsR = deque()

    with open('num_ls.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            nums = line.strip().split()
            for i in range(len(nums)):
                num = int(nums[i])
                if i == 0:
                    numsL.append(num)
                else:
                    numsR.append(num)
    
    numsL = deque(sorted(numsL))
    # print(numsL)
    numsR = deque(sorted(numsR))
    # print(numsR)
    nums = deque()
    total = 0
    found = {}
    while len(numsL) > 0:
        numL = numsL.popleft()
        
        if numL in found:
            print(f"Num: {numL} | Overlap: {overlap} | Score: {score} | Total: {total}")
            total += found[numL]
            continue

        overlap = 0
        while numsR[0] <= numL:
            numR = numsR.popleft()
            if numR == numL:
                overlap += 1
            if len(numsR) == 0:
                break
        score = numL * overlap
        total += score
        print(f"Num: {numL} | Overlap: {overlap} | Score: {score} | Total: {total}")
        found[numL] = numL * overlap
        if len(numsR) == 0:
            break
    print(f"Similarity Score: {total}")
    print(min(False, 2))

    
if __name__ == "__main__":
    main()