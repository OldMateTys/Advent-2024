from collections import deque

def flatten(data, pages):
    ls = deque(sorted(data))
    output = deque()
    #print(ls)
    while len(ls) > 0:
        
        first_num = 0
        for num1 in ls.copy():
            found = False
            for num2 in ls.copy():
                if num1 == num2:
                    continue

                if num1 in data[num2]:
                    found = True
            
            if not found:
                first_num = num1
                break
        output.append(first_num)
        # print(first_num, data)
        for item in data:
            if first_num in data[item]:
                data[item].remove(first_num)
        # print(ls)
        del data[first_num]
        ls.remove(first_num)
        
    # print(output)
    return list(output)[::-1]


def run(data, pages, order):

    count = 0
    total = 0
    for page in pages:
        page = set(page)
        

        if valid:
            count += 1
            total += page[len(page) // 2]
            #print(f"Added: {page} | Total: {total}")
    # print(count)

def disallow(num: int, data: dict[set]):
    if num not in data:
        return set()
    if len(data[num]) == 0:
        return set()
    
    dataSet = data[num]
    # print(data[num])
    dataAdd = set()
    for item in dataSet:
        mySet = disallow(item, data)
        # print(item, mySet)
        dataAdd.update(mySet)
    dataAdd.update(dataSet)
    return dataAdd

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
    rules2 = {}
    for item in rules:
        rules2[item] = disallow(item, rules)
        #print(rules2[item])
    #print(rules2)
    order = flatten(rules2, pages)
    print(order)
    run(rules2, pages, order)
    

if __name__ == "__main__":
    main()