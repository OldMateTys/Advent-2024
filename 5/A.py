from collections import deque

def iterate(data, pages):
    pass

def run(rules, pages):

    count = 0
    total = 0
    fixCount = 0
    fixTotal = 0
    banSet = set()
    for i, page in enumerate(pages):
        
        banSet = set()
        valid = True
        for num in page:
            if num in banSet:
                valid = False
                break
            banSet.update(rules[num])
        
        count += page[len(page) // 2] if valid else 0
        print(f"Valid page: {page}")
        print(f"Midpoint: {page[len(page) // 2]}")
        print()
    print(count)

def disallow(num: int, data: dict[set], depth):
    print(num)
    if depth == 100:
        print("100 Deep. Exiting.")
        exit()
    
    memo = {}
    # print(data)
    def apply(num, data):
        if num not in data:
            return set()
        if len(data[num]) == 0:
            return set()
        if num in memo:
            return memo[num]

        dataSet = data[num]
        # print(data[num])
        dataAdd = set()
        for item in dataSet:
            #print(item)
            
            mySet = disallow(item, data, depth + 1)
            # print(item, mySet)
            dataAdd.update(mySet)
        dataAdd.update(dataSet)

        memo[num] = dataAdd
        return dataAdd

    mySet = apply(num, data)
    return mySet


def main():
    
    first = True
    rules = {}
    pages = deque()
    with open('rules.txt', 'r') as file:
        for i, line in enumerate(file.readlines()):
            # print(rules)
            if line.isspace():
                #print('here')
                first = False
                continue
            if first:
                
                nums = line.strip().split('|')
                #print(nums)
                num1 = int(nums[0])
                num2 = int(nums[1])
                if num1 not in rules:
                    rules[num1] = set()
                if num2 in rules:
                    rules[num2].add(num1)
                else:
                    rules[num2] = set([num1])
                
            else:
                ls = line.strip().split(',')
                for i in range(len(ls)):
                    ls[i] = int(ls[i])
                pages.append(ls)
        # print(ls)
    #print(rules)
    
    for line in sorted(rules):
        print(f"{line}: {rules[line]}")
    rules2 = {}

    run(rules, pages)

    

if __name__ == "__main__":
    main()