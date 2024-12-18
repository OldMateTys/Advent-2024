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
        print(f"Total: {total}")

    def recur(self, ls: deque, total, target):
        
        
        if len(ls) == 0:
            if total == target:
                return True
            return False
        new_ls = ls.copy()
        num = new_ls.popleft()

        
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
            ls = line.strip().split(" ")
            num_list = deque()
            target = 0
            for i, num in enumerate(ls):
                if i == 0:
                  
                    target = int(num[:-1])
                    continue
                num_list.append(int(num))
            if target not in nums:
                nums[target] = [num_list]
            else:
                nums[target].append(num_list)
    

    s = Solution(nums)
    s.run()

if __name__ == "__main__":
    main()