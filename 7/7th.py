import math
from collections import deque

class Solution:

    nums = {}

    def __init__(self, nums):
        self.nums = nums

    def run(self):

        total = 0

        for i, num in enumerate(self.nums):
            for ls in self.nums[num]:

                if self.recur(ls.copy(), 0, num):
                    total += num
                    # print(f"Successful: {num}")
                print(f"Progress: {i} / {len(self.nums)}")
        print(total)

    def recur(self, ls: deque, total, target):
        
        
        if len(ls) == 0:
            # # print(f"Total: {total} | Target: {target} | ls: {ls}")
            if total == target:
                # # print("True returned")
                return True
            return False
        new_ls = ls.copy()
        num = new_ls.popleft()
        # print(f"Total: {total} | Next: {num} | Target: {target} | ls: {new_ls}")

        
        mult_total = total * num
        if mult_total == 0:
            mult_total = num
        add_total = total + num
        add = self.recur(new_ls, add_total, target)
        mult = self.recur(new_ls, mult_total, target)

        num_len = math.floor(math.log10(num)) + 1
        concat_total = total * 10 ** num_len + num
    
        concat = self.recur(new_ls, concat_total, target)

        return add or mult or concat
        





def main():
    
    nums = {}

    with open('math.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            # print(line)
            ls = line.strip().split(" ")
            # print(ls)
            num_list = deque()
            target = 0
            for i, num in enumerate(ls):
                if i == 0:
                    # print(f"'{num[:-1]}'")
                  
                    target = int(num[:-1])
                    continue
                num_list.append(int(num))
            if target not in nums:
                nums[target] = [num_list]
            else:
                nums[target].append(num_list)
    
    # print(nums)

    s = Solution(nums)
    s.run()

if __name__ == "__main__":
    main()