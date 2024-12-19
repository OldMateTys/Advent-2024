def towels(towel: str, comboSet: set, memo: set):
    if len(towel) == 0:
        return 1
    if towel in memo:
        return memo[towel]
    
    count = 0
    for combo in comboSet:

        if len(towel) < len(combo):
            continue
        if towel[:len(combo)] != combo:
            continue
        newTowel = towel[len(combo):]
        num = towels(newTowel, comboSet, memo)
        memo[newTowel] = num
        count += num
    
    return count

def parseInput(filename):

    towelList = []
    comboSet = []
    
    with open(filename, 'r') as file:
        
        lines = file.readlines()
        comboSet = set([x.strip() for x in lines[0].split(",")])
        towelList = [line.strip() for i, line in enumerate(lines) if i > 1]
        print(towelList)

    return towelList, comboSet

def main():
    towelList, comboList = parseInput('input.txt')
    memo = {}
    count = sum(towels(towel, comboList, memo) for towel in towelList)
    print(f"Count: {count}")
    

main()