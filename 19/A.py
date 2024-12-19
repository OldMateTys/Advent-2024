def towels(towel, comboSet):
    if len(towel) == 0:
        return True
    
    for combo in comboSet:
        # print(combo)
        # print(towel)
        if len(towel) < len(combo):
            continue
        if towel[:len(combo)] != combo:
            continue
        if towels(towel[len(combo):], comboSet):
            return True
    
    return False

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
    count = sum(1 for towel in towelList if towels(towel, comboList))
    print(f"Count: {count}")
    

main()